---
Title: Cisco DHCP Pool convertion to Windows Server DHCP
Date: 2024-10-13 16:00
Status: published
Category: Network DevOps
Tags: DHCP, Windows, PowerShell, Cisco
Keywords: DHCP, Windows, PowerShell, Cisco
Slug: 2024-10-13-cisco-dhcp-conversion-to-windows-server
Image: ciscodhcp.png
Author: Justin Cooksey
Summary: A Windows Powershell script to ease the transition from Cisco config DHCP Pools to a Windows DHCP server.  Convert from an exported Cisco config direct in to DHCP Server
---


<img src="{attach}ciscodhcp.png"  width="33%" height="33%">

**Well it was bound to happen!**
Three years now after being asked to migrate DHCP from Windows DHCP server to Cisco Routers, and automating that convertion, [which you can read about here](https://justincooksey.com/blog/2021/2021-03-04-windows-server-dhcp-conversion-to-cisco-cli), it's finally going back the other way.

This time the PowerShell script will read through the file (an exported Cisco Router configuration) and build the Scopes in the Windows DHCP Role.  The script will need to be run on the server becoming the DHCP server fro the new scopes.  All of this could be expanded on to make it more versatile, but at this point it wasnt required.

The script initally reads through and using Regular Expressions finds DHCP Pools (Scopes) configured in the router config
Follows by finding and adding exclusions to those Scopes
Then will find and set any static IPO assignments for specific devices.

Some DHCP Options are being handled aslisted below.

#### DHCP Options Handling

| Code | Cisco Config     | Option Description      |
| ---- | ---------------- | ----------------------- |
| 3    | default-router   | Default Gateway         |
| 6    | dns-server       | Domain Nameservers      |
| 15   | domain-name      | Domain Name             |
| 42   | option 42 ip     | NTP Servers             |
| 43   | option 43 hex    | Vendor Specific Option  |
| 51   | lease            | Lease time              |
| 66   | next-server      | TFTP Server             |
| 66   | option 66 ip     | TFTP Server             |
| 67   | bootfile         | Boot filename           |
| 67   | option 67 ascii  | Boot filename           |

[Code Repository can be found on GitHub](https://github.com/jscooksey/cisco-dhcp)

Making use of the [IPv4Calc Module](https://www.powershellgallery.com/packages/IPv4Calc)