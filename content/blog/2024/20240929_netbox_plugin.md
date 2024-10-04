---
Title: Netbox Plugin
Date: 2024-09-29 16:00
Status: published
Category: Network DevOps
Tags: Network, Netbox, Python, Django, DevOps
Keywords: Network, Netbox, Django, DevOps
Slug: 2024-09-29-netbox-plugin
Author: Justin Cooksey
Summary: Developing a Netbox Plugin to process a defined set of rules to manage aloocation of resources in multi-tenant infrastructure of network and hosting.
---

<img src="{attach}netbox.png"  width="33%" height="33%">

Working with [Netbox](https://netboxlabs.com/docs/netbox/en/stable/introduction/) as recpord keeping for multi-tenant infrastructure has shown it to be an extremely powerful tool used as a Source Of Truth in the network.  All chnages must be recorded in Netbox before pushed to the actual system.  This meant that a significant amount of work for any change could be automated in Netbox as well.  A new Fibre service, and new SIP service and new hosted server network.  These all involved selection of certain VLANs, VRFs, Subnets to be allocated to a Tenant within the infrastructure.

Initially when [Netbox](https://netboxlabs.com/docs/netbox/en/stable/introduction/) was first implemented I developed a series of [Netbox Custom Scripts](https://netboxlabs.com/docs/netbox/en/stable/customization/custom-scripts/) to run through these choices and build a new service for a Tenant.  This has worked for some time witout issue, but in needing to upgrade [Netbox](https://netboxlabs.com/docs/netbox/en/stable/introduction/) to more recent versions the Script method does not really continue to work well and the collection of Scripts really neeed to be rbought in to its own [Netbox Plugin](https://netboxlabs.com/docs/netbox/en/stable/plugins/).
