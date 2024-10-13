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
Three years now after being asked to [migrate DHCP from Windows DHCP server to Cisco Routers, and automating that convertion, which you can read about here](https://justincooksey.com/blog/2021/2021-03-04-windows-server-dhcp-conversion-to-cisco-cli), it's finally going back the other way.

This time the PowerShell script will read through the file (an exported Cisco Router configuration) and build the Scopes in the Windows DHCP Role.  The script will need to be run on the server becoming the DHCP server fro the new scopes.  All of this could be expanded on to make it more versatile, but at this point it wasnt required.

The script follows these steps:

1. Reads through the configuration file and, using Regular Expressions, finds all DHCP Pools (Scopes), Static Assignments and Exclusions.
2. Creates all the Scopes, along with all options found under that Pool in the router configuration file.
3. Processes the Exclusions in to each Scope
4. Process all static assignments


Some DHCP Options are being handled as listed below.

#### DHCP Options Handling

| Code | Cisco Config     | Option Description         |
| ---- | ---------------- | -------------------------- |
| 3    | default-router   | Default Gateway            |
| 6    | dns-server       | Domain Nameservers         |
| 15   | domain-name      | Domain Name                |
| 42   | option 42 ip     | NTP Servers                |
| 43   | option 43 hex    | Vendor Specific Option, usually WAP Controller IP |
| 51   | lease            | Lease time                 |
| 66   | next-server      | TFTP Server                |
| 66   | option 66 ip     | TFTP Server                |
| 67   | bootfile         | Boot filename              |
| 67   | option 67 ascii  | Boot filename              |

[Code Repository can be found on GitHub](https://github.com/jscooksey/cisco-dhcp)

**Example Cisco Config**
```text
ip dhcp excluded-address 10.10.0.1 10.10.1.0
ip dhcp excluded-address 10.10.3.220 10.10.3.223
ip dhcp excluded-address 192.168.0.1 192.168.0.9
!
ip dhcp pool PoolNumber1
 network 10.10.0.0 255.255.248.0
 update dns both override
 dns-server 10.10.255.1 10.10.255.2 
 domain-name domainname.local
 option 42 ip 10.10.249.11 10.10.248.11 
 default-router 10.10.0.1 
 lease 8
!
ip dhcp pool PoolNumber2
 network 192.168.0.0 255.255.255.0
 dns-server 192.168.0.10
 option 43 hex f108.0afe.0064
 default-router 192.168.0.1
!
ip dhcp pool Device1
 host 10.10.1.30 255.255.248.0
 client-identifier 01b7.37eb.1f1a.0a
 default-router 10.10.0.1 
!
ip dhcp pool Device2
 host 192.168.0.44 255.255.255.0
 client-identifier 0132.c19f.b7f3.3b

```

Making use of the [IPv4Calc Module](https://www.powershellgallery.com/packages/IPv4Calc)