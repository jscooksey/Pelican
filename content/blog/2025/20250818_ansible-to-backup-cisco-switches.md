---
title: Using Ansible to backup Cisco SMB switches
date: 2025-08-18 21:00
status: published
category: Network DevOps
tags: Ansible, Cisco, Network, backup, Netbox
keywords: Ansible, Cisco, Network, backup, netbox
slug: 2025-08-18-ansible-to-backup-cisco-switches
author: Justin Cooksey
image: ansible_backup.png
description: With Netbox as a source of truth (SoT) we use an Ansible playbook to manage the regular backups of Cisco switch configurations.  Then using a bash script to upload those to a DR site in case of failure of our local storage.
---

![Ansible Backup]({attach}ansible_backup.png){: .image-process-large-photo}

# Using Ansible to Backup Cisco SMB Switches  

With [NetBox](https://netbox.dev/) as a source of truth (SoT), we can use an [Ansible](https://docs.ansible.com/ansible/latest/index.html) playbook to perform regular backups of Cisco switch configurations. To add an extra layer of resilience, a simple bash script can then upload those backups to a disaster recovery (DR) site.  

This post builds on my [earlier article on using Ansible with NetBox](https://justincooksey.com/blog/2024/ansible-netbox-begining), but here we’ll go deeper into the backup process and how to automatically offload files to an external location.  

---

## Why Back Up Switch Configurations with Ansible?  

Switch configuration backups are often overlooked until something breaks. Using Ansible for backups provides:  

- **Automation** – run backups daily without manual effort.  
- **Consistency** – identical process across all devices.  
- **Versioning** – timestamped configs make rollbacks easy.  
- **Resilience** – copy backups to a DR site in case local storage fails.  

---

## The Ansible Playbook  

This playbook uses the [Ansible Community Cisco SMB collection](https://docs.ansible.com/ansible/latest/collections/community/ciscosmb/index.html), which supports Cisco Small and Medium Business switches such as SG300, SG500, SG350, SG550, CBS350, and C1300. The approach is easily adaptable to other Cisco or network devices.  

NetBox provides the inventory, filtered to only include switches (`hosts: device_roles_switch`). Credentials for both NetBox and devices are securely stored in [Ansible Vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html).  

Here’s the playbook:  

```yaml
- name: Backup Switch Configs
  gather_facts: no
  hosts: device_roles_switch
  
  vars_files:
    - ~/ansible/vaults/secrets.yml

  vars:
    ansible_network_os: community.ciscosmb.ciscosmb
    ansible_connection: network_cli
    ansible_become: true
    ansible_become_method: enable
    output_path: "/home/backups/"

  tasks:
    # Create backup folder for today
    - name: Get date stamp for filename creation
      set_fact: date="{{ lookup('pipe','date +%Y%m%d') }}"
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

This will generate timestamped configuration files such as:  

```
/home/backups/SWITCH01-20250721.txt
```

---

## Scheduling the Backup  

To keep backups up to date, schedule the playbook with `cron` (or your favorite scheduler) to run daily. This ensures you always have the latest configuration stored locally.  

---

## Offloading to a Disaster Recovery Site  

Local backups are good, but if the Ansible host is lost, those files go with it. To prevent that, we can push backups offsite.  

Here’s a simple bash script that:  

1. Removes backups older than 14 days.  
2. Uploads only today’s backups (filtered by date string) to an FTP server.  

```bash
# stored elsewhere, e.g. environment variables
# HOST, USER, PASSWD

FOLDER=~/backups/
DATE=$(date +%Y%m%d)

# Clean out local backups older than 14 days
find "$FOLDER" -type f -mtime +14 -exec rm {} \;

cd "$FOLDER" || exit

# FTP today’s files
ftp -n $HOST <<END_SCRIPT
quote USER $USER
quote PASS $PASSWD
cd switches
prompt off
mput *$DATE*
quit
END_SCRIPT

exit 0
```

> 🔐 Note: For production use, consider SFTP or HTTPS-based storage instead of plain FTP for stronger security.  

---

## Wrapping Up  

With just a lightweight playbook and a small shell script, you can:  

- Back up all Cisco SMB switch configurations daily.  
- Store them with clear timestamps for easy tracking.  
- Automatically offload them to a DR site.  

From here, you can expand the workflow by:  

- Integrating monitoring to alert if a backup fails.  
- Using a more secure remote storage option.  
- Automating config diff reports for change tracking.  

This small setup provides a big step toward resilient, automated network management.  