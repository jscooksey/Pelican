---
Title: Using Ansible to Maintain Cisco SMB Products
Date: 2023-07-31 14:00
Status: draft
Category: Network DevOps
Tags: Ansible, Network, DevOps, Cisco
Keywords: Ansible, Network, DevOps, Cisco
Slug: ansible-ciscosmb
Author: Justin Cooksey
Image: ansible.png
Summary: Using Ansible to audit, backup, update and maintain a group of Cisco Small to Medium Business Solutions such as the CBS range of switches.
---

Ansible is not just for the high end data centre systems and servers, but it can also be used on large scale systems that are using small to medium business systems such as the [Cisco SMB Product](https://www.cisco.com/c/en_au/solutions/small-business.html#~products) range of switches and routers.

## Auditing

Auditing devices to get serial numbers, firmware versions, models

## Minimum config

Ensuring all devices have
- NTP
- SNMP
- SSH only

## Backup config
 copying config on all devices
 
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
