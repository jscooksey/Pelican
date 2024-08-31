---
Title: Netbox and Ansible for for Small to Mid Business Networks
Date: 2024-08-31 14:00
Status: published
Category: Network DevOps
Tags: Ansible, Network, Netbox, DevOps, Cisco
Keywords: Ansible, Network, Netbox, DevOps, Cisco
Slug: ansible-netbox-begining
Author: Justin Cooksey
Summary: Using Ansible and Netbox to audit, backup, update and maintain a group of Cisco Small to Medium Business Solutions such as the CBS range of switches.
---

[Ansible](https://docs.ansible.com/ansible/latest/index.html) and [Netbox](https://netboxlabs.com/docs/netbox/en/stable/) are not just for the high end data centre systems.  They can also be used on networks using small to medium business switches and routers such as the [Cisco SMB Product](https://www.cisco.com/c/en_au/solutions/small-business.html#~products) range.


## Initial Auditing and OnBoarding

Initally I started with brand new empty [Netbox](https://netboxlabs.com/docs/netbox/en/stable/). In which I manually created a base setup adding in each:

- Site
- Patch
- Device model in use
- Prefix, to begin with just the management subnets

Then creating a yaml file host listing to beging with, I ran an [Ansible](https://docs.ansible.com/ansible/latest/index.html) Playbook that then went through that list of devices pulling base device information:

- IP Address (Management)
- Hostname
- Model
- Serial number
- Firmware  (*This was not initally used*)

This was then to record in to [Netbox](https://netboxlabs.com/docs/netbox/en/stable/) as new devices as well as exported to CSV.  After I had the devices in [Netbox](https://netboxlabs.com/docs/netbox/en/stable/) I could do some base housekeeping and put them in the right sites, patches and rack locations.


## [Netbox](https://netboxlabs.com/docs/netbox/en/stable/), the Source of Truth

Once the devices were in and housekeeping done [Netbox](https://netboxlabs.com/docs/netbox/en/stable/) then became the [Source of Truth](https://netboxlabs.com/blog/what-is-a-network-source-of-truth/) for both our engineers and technicians and also for [Ansible](https://docs.ansible.com/ansible/latest/index.html).  I could remove the hosts yaml file an dpointing AQnsible at Netbox for its inventory I could now allow playbooks to be run against a site and other locations or across the whole group.


## Minimum config

One of the frist tasks was to ensure I had all devices, configured to a standard.  I hoped that they have been, but over time, without continued audits and checks, things can become a little out.  So using [Ansible](https://docs.ansible.com/ansible/latest/index.html) I was able to ensure some defaults are set, such has:

- Disabling of access methods, such as HTTP, Telnet and also HTTPS
- NTP time servers and synchronised time
- Name Servers
- Monitoring service setting (SNMP)


## Backup config

Another task for [Ansible](https://docs.ansible.com/ansible/latest/index.html) was to get regular configuration backups for all devices.  Running an [Ansible](https://docs.ansible.com/ansible/latest/index.html) Playbook on a daily schedule (Cron) to pull the current configuration and store it on the local file system of the [Ansible](https://docs.ansible.com/ansible/latest/index.html) server.  This was then replicated off site over secure protocols.
 
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

## Finding Trunks and Devices

Another task was find all the trunks between switches & patches and docuemnt them correctly in Netbox.  Running an [Ansible](https://docs.ansible.com/ansible/latest/index.html) Playbook to use LLDP from gather facts to then determine th elinks between device, that could then be documented as Netbox cables.  Once that was done I also used the [Netbox Topology Views](https://github.com/netbox-community/netbox-topology-views) plugin to visualise the network.

Once that was done I could also use MAC address searches to determine what ports IP Phones, DAPs and WAPs were connected to among other devices.  Since a standard brand of those was used throughout it was only a matter of searching for the manufacturer portion of the MAC address.