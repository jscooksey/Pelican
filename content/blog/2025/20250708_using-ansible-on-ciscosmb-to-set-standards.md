---
title: Using Ansible to set standards across Cisco SMB Switches
date: 2025-07-08 16:00
status: published
category: Network DevOps
tags: Ansible, Cisco, Network, backup, Netbox
keywords: Ansible, Cisco, Network, backup, Netbox
slug: 2025-07-08-using-ansible-on-ciscosmb-to-set-standards
author: Justin Cooksey
image: ansible_netbox_cisco_600.jpg
description: Using Ansible to set switch configuration standards across a fleet of Cisco Small Medium Business switches (SG300, SG500, SG350, SG550, CBS350, C1300). Maintaining a default setup for DNS, Time and Date and allowed access methods.
---
 
<img class="image-process-large-photo"src="{attach}ansible_netbox_cisco_600.jpg">

I covered some of the base configuration in a [previous article](https://justincooksey.com/blog/2024/ansible-netbox-begining) on how Netbox and Ansible work together.  This time I'm covering working with the [Ansible Community Cisco SMB collection](https://docs.ansible.com/ansible/latest/collections/community/ciscosmb/index.html) to manage Cisco Small and Medium Business switches in the ranges SG300, SG500, SG350, SG550, CBS350 and C1300. 

The source of truth in this environment is [Netbox](https://netbox.readthedocs.io/en/feature/introduction/) IPAM.  As before Netbox is being used for Ansibles inventory via the [Netbox Namespace collection](https://docs.ansible.com/ansible/latest/collections/netbox/netbox/index.html).

## Setting the Standard
New switches will get a standard configuration by first adding them in to Netbox and then creating the configuration using Netbox [Configuration Rendering](https://netbox.readthedocs.io/en/feature/features/configuration-rendering/).  This playbook is used to bring current switches to a standard, enforcing that standard and/or applying any new changes to the standards.  Setting standards such as keeping them all on a set timezone as well as the same time, domain name servers, and security methods controlling access and password policies.

To make it easier to explain I'm splitting these in to different tasks.  They could all be run as one task, but this way is easier to explain what each part is trying to achieve.

## Start of the Playbook
Setting the stage for the rest of the playbook.
1. No need to spend time getting [device facts](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/gather_facts_module.html), so **gather_facts** run so its set to **false**
2. Selecting only the switches from inventory by setting **hosts** as **device_roles_switch**. This will pick only the switches from Netbox device list based on each device in Netbox having the **Device Role** field correctly set.
3. Loading variables/secrets to be used for SSH connections as well as the Netbox API from an [Ansible Vault](https://docs.ansible.com/ansible/latest/vault_guide/vault.html) file **secrets.yml**
4. Setting other default variables for running the playbook
```yaml
- name: Standard Switch Configuration
  gather_facts: false
  hosts: device_roles_switch
  
- vars_files:
    - ~/ansible/vaults/secrets.yml

  vars:
    ansible_network_os: community.ciscosmb.ciscosmb
    ansible_connection: network_cli
    ansible_become: true
    ansible_become_method: enable
    
  tasks:
```

## Basic TCP/IP Network Settings
Setting the basic network network settings.  This will allow for changing the domain name servers across the board if that has to happen at some future point.
1. Setting the IP address of name servers (DNS) using **ip name-server**. 
2. Setting the default domain name to be used on name lookups using **ip domain name**.
```yaml
    - name: Set Base Network (DNS)
      community.ciscosmb.command:
        commands:
          - configure terminal
          - ip name-server 192.168.1.2 192.168.2.2
          - ip domain name domainname.local
          - exit
```

## Setting and Syncing Time and Date
While it's potentially a good idea to simply set all devices to a set timezone, such as UTC and then, I thought Id include the other option of using a local timezone and even incorporating daylight savings changes.  With this setup the switch logs will always be on the local time of those looking at them, assuming we aren't talking timezone spanning businesses.
1. Set the timezone code and its difference from UTC
2. Set the daylight savings start and end points
3. Set the NTP servers to sync time from.
4. Ensure the source is set to use those NTP servers
```yaml
    - name: Set Time Settings (Timezone & SNTP)
      community.ciscosmb.command:
        commands:
          - configure terminal
          - clock timezone AEST +10
          - clock summer-time AEDT recurring first sun oct 02:00 first sun apr 03:00
          - sntp server 192.168.1.3 poll
          - sntp server 192.168.2.3 poll
          - clock source sntp
          - exit
```

## Securing
We only need the one secure method of access, and SSH is it.
1. Disabling Telnet, HTTP and HTTPS access
```yaml
    - name: Disable HTTP(S) and Telnet
      community.ciscosmb.command:
        commands:
          - configure terminal
          - no ip http server
          - no ip http secure-server
          - no ip telnet server
          - exit
```

2. Set password security  limits, but disabling ageing of the password being enforced by the switch
```yaml
    - name: Set Password Security
      community.ciscosmb.command:
        commands:
          - configure terminal
          - passwords aging 0
          - passwords complexity min-length 12
          - exit
```

## Completed
Finally we can clearly add more in if there are other standard that need to be kept.  Otherwise
we write the config to the switch. 

```yaml
    - name: Write Config Changes
      community.ciscosmb.command:
        commands:
          - wr mem
```

## Conclusion
Not the most complicated playbook, but a useful one to get and keep everything at a set standard.  Among other options, if you want to collect logs centrally another addition would be to set a syslog server to collect all logs from each device centrally.