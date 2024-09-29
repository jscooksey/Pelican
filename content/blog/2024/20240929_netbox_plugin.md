---
Title: Netbox Plugin
Date: 2024-09-29 16:00
Status: draft
Category: Network DevOps
Tags: Network, Netbox, Python, Django, DevOps
Keywords: Network, Netbox, Django, DevOps
Slug: 2024-09-29-netbox-plugin
Author: Justin Cooksey
Summary: Developing a Netbox POlugin to handle defined set of rules used by network and hosting infrastructure to allocate VLANs, VRF and handle Tenants
---

<img src="{attach}ciscodhcp.png"  width="33%" height="33%">

Well it was bound to happen! After being asked to migrate DHCP from Windows DHCP server to Cisco devices, and automating that convertion, [which you can read about here](https://justincooksey.com/blog/2023/pelican-static-site-generator.html), it's finally going back the other way.



Making use of the [IPv4Calc Module](https://www.powershellgallery.com/packages/IPv4Calc)

We first pull out the various Pools and create the equivalent Windows Scopes, then porcess the exclusions that need to be added to each scope.  Finally running through the static assignments to different devices.

Still ha smany DHCP options that it hasn't been setup to hanle at this point but it does follow the basic ones that most of us use.
