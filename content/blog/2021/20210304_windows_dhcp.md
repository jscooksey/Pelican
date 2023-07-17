---
Title: Windows Server DHCP conversion to Cisco CLI
Date: 2021-03-04 08:00
Category: Article
Tags: DHCP, Windows, PowerShell, Cisco
Slug: 2021-03-04-windows-server-dhcp-conversion-to-cisco-cli
Author: Justin Cooksey
Image: dhcp.jpg
Summary: A Windows Powershell script to ease the transition from a Windows DHCP server to a Cisco router DHCP. Convert from a backup to the Cisco command line.
---

<img src="{attach}dhcp.jpg"  width="33%" height="33%">

I recently ran in to an issue where I needed to convert a reasonably large DHCP database from a Windows Server in to a Cisco CLI to allow the Cisco to take over DHCP roles for a subnet. I found nothing that realy automated this task, even using the exported XML file. So knowing that this was the second time I needed the tool, and likely to need it again, even if it was for smaller tasks, I set about coding it in Powershell. It is the scripting system well supported in Windows land.

The current version of the script can be found on my GitHub repository:
[Convert-WindowsDHCPToCisco](https://github.com/jscooksey/Convert-WindowsDHCPToCisco)

Still ha smany DHCP options that it hasn't been setup to hanle at this point but it does follow the basic ones that most of us use.

#### Currently handles DHCP Options

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
