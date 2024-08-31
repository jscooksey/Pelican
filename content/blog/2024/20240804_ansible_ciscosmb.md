---
Title: Netbox and Ansible to Maintain Cisco SMB Products
Date: 2024-08-04 14:00
Status: draft
Category: Network DevOps
Tags: Ansible, Network, Netbox, DevOps, Cisco
Keywords: Ansible, Network, Netbox, DevOps, Cisco
Slug: netbox-ansible-beginings
Author: Justin Cooksey
Image: ansible.png
Summary: Using Ansible and Netbox to audit, backup, update and maintain a group of Cisco Small to Medium Business Solutions such as the CBS range of switches.
---

[Ansible](https://docs.ansible.com/ansible/latest/index.html) and [Netbox](https://netboxlabs.com/docs/netbox/en/stable/) are not just for the high end data centre systems.  They can also be used on large scale systems that are using small to medium business systems such as the [Cisco SMB Product](https://www.cisco.com/c/en_au/solutions/small-business.html#~products) range of switches and routers.

## Initial Auditing and OnBoarding

Initally I had nothing recorded in [Netbox](https://netboxlabs.com/docs/netbox/en/stable/). I cvreated a base of each of the sites and patch panels at each site, as well as all the device models that were in use.

Ran an Ansible Playbook that then went through the list of devices pulling base device information to record in [Netbox](https://netboxlabs.com/docs/netbox/en/stable/).  After I had the devices in I could do some management and put them in the right sites, patches and rack locations.

Auditing devices to get serial numbers, firmware versions, models
1. [Netbox](https://netboxlabs.com/docs/netbox/en/stable/)
  - Hostname is device name in netbox
  - Serial Number
  - Model
  - Firmware version to platforms
2. Exported to CSV


## [Netbox](https://netboxlabs.com/docs/netbox/en/stable/), the Source of Truth

Once the devices were in and some management had been done to get them in the right locations etc.  [Netbox](https://netboxlabs.com/docs/netbox/en/stable/) then became the [Source of Truth](https://netboxlabs.com/blog/what-is-a-network-source-of-truth/) for both our engineers and technicians but also for Ansible.  Allowing playbooks to be run against site and locations only or across the whole group.

## Minimum config

One of the frist tasks was to ensure we had all devices, configured to s standard.  We hoped that they have been, but over time, without audits and checks, things can become a little out.  So using Ansible we have been able to ensure some defaults are set, such has:
  - Disabling of access methods, such as HTTP, Telnet and also HTTPS
  - NTP time servers and synchronised time
  - Name Servers
  - Monitoring service setting (SNMP)

## Backup config
Another task for Ansible was to get regular configuration backups for al devices.  Running an Ansible Playbook on a schedule (Cron) to poull the current configuration and store it on the local file system of the Ansible server.  This was then replicated off site over secure protocols.
 
```yaml
- name: Gather Facts
  gather_facts: no
  hosts: device_roles_switch
  vars:
    output_path: "{{ lookup('env', 'HOME') }}/backups/"

  tasks:
    ## Create backup folder for today
    - name: Get date stamp for filename creation
      set_fact: date="{{lookup('pipe','date +%Y%m%d')}}"
      run_once: true

    # Get Switch Config
    - name: Get Config
      community.ciscosmb.facts:
        gather_subset:
          - config

    - name: Save Config
      copy:
        content: "{{ ansible_net_config }}"
        dest: "{{ output_path }}{{ inventory_hostname }}-{{ date }}.txt"
```
