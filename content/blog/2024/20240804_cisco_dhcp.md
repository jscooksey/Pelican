---
Title: Cisco DHCP Pool convertion to Windows Server DHCP
Date: 2024-08-04 14:00
Status: draft
Category: Network DevOps
Tags: DHCP, Windows, PowerShell, Cisco
Keywords: DHCP, Windows, PowerShell, Cisco
Slug: 2021-03-04-cisco-dhcp-conversion-to-windows-server
Image: ciscodhcp.png
Author: Justin Cooksey
Summary: A Windows Powershell script to ease the transition from Cisco config DHCP Pools to a Windows DHCP server.  Convert from an exported Cisco config direct in to DHCP Server
---


<img src="{attach}ciscodhcp.png"  width="33%" height="33%">

Well it was bound to happen! After being asked to migrate DHCP from Windows DHCP server to Cisco devices, and automating that convertion ([Which you can read about here](https://justincooksey.com/blog/2023/pelican-static-site-generator.html))), it's finally going back the other way.





Still ha smany DHCP options that it hasn't been setup to hanle at this point but it does follow the basic ones that most of us use.

#### Need to chnage this

| Code | Option Description      | Cisco Output     |
| ---- | ----------------------- | ---------------- |
| 3    | Default Gateway         | default-router   |
| 4    | Time Server             | _ignoring_       |
| 6    | Domain Nameserver       | dns-server       |
| 15   | Domain Name             | domain-name      |
| 42   | NTP Servers             | option 42 ip     |
| 51   | Lease time              | _ignoring_       |
| 66   | TFTP Server             | next-server      |
| 67   | Boot filename           | bootfile         |
| 81   | MS DHCP Name Protection | _ignoring_       |
| 121  | Static routes           | option 121 hex   |
| 161  | FTP Server              | option 161 ip    |
| 162  | Path                    | option 162 ascii |
| 252  | Proxy PAC URL           | option 252 asicc |

#### DHCP References Used

- [RFC2312](https://tools.ietf.org/html/rfc2132)
- [Wikipedia DHCP Options table](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol#Client_configuration_parameters)
