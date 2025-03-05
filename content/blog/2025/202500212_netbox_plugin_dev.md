---
Title: Netbox Plugin Development
Date: 2025-02-12 16:00
Status: draft
Category: DevOps
Tags: Python, Code, Netbox, DevOps, Django, Plugin, MSP
Keywords: Python, Netbox, DevOps, Django, plugin, msp
Slug: 2025-02-12-netbox-plugin-dev
Author: Justin Cooksey
Image: netbox.png
Summary: After slowly adding scripts to automate tasks in Netbox, it became apparent that it would be more effective to imoplement them all in a Netbox (Django) plugin.  These are some notes covering my migration to a plugin.
---

Development issue VPN IDs
  - Incoming Services
    - WAN connection over Fibre, NBN etc
    - SIP
  - Hosted networks for vitual machines

<img src="{attach}netbox.png"  width="33%" height="33%">


Issuing Public IPs from our pool of addresses

Building configs based off Jinja2 templates to confiure the core firewall and LNS

Configure the RADIUS server for services requiring authentication

Own procedures in selecting these vlans etc

Keeping this up to date under Tenants

moveds from a set of scripts under 3. version to a plugin

Using a docker image with data copied from live for testing

[Pypi server](https://github.com/pypiserver/pypiserver), common internal serevr that can bve seen from production and development.  Production is limiting it version of the plugin and development moves ahead of that






