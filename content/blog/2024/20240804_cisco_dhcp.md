---
Title: Cisco DHCP Pool convertion to Windows Server DHCP
Date: 2024-10-04 14:00
Status: published
Category: Network DevOps
Tags: DHCP, Windows, PowerShell, Cisco
Keywords: DHCP, Windows, PowerShell, Cisco
Slug: 2021-03-04-cisco-dhcp-conversion-to-windows-server
Author: Justin Cooksey
Summary: A Windows Powershell script to ease the transition from Cisco config DHCP Pools to a Windows DHCP server.  Convert from an exported Cisco config direct in to DHCP Server
---


<img src="{attach}ciscodhcp.png"  width="33%" height="33%">

Well it was bound to happen! After being asked to migrate DHCP from Windows DHCP server to Cisco devices, and automating that convertion, [which you can read about here](https://justincooksey.com/blog/2023/pelican-static-site-generator.html), it's finally going back the other way.



Making use of the [IPv4Calc Module](https://www.powershellgallery.com/packages/IPv4Calc)

We first pull out the various Pools and create the equivalent Windows Scopes, then porcess the exclusions that need to be added to each scope.  Finally running through the static assignments to different devices.

Still ha smany DHCP options that it hasn't been setup to hanle at this point but it does follow the basic ones that most of us use.

end.