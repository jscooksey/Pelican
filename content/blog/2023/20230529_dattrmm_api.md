---
Title: Datto RMM API Sites Export
Date: 2023-05-29 12:30
Status: published
Category: Network DevOps
Tags: Python, Code, RMM, DattoRMM, API
Keywords: Python, Code, RMM, DattoRMM, API
Slug: dattormm-api
Author: Justin Cooksey
Image: dattormm.png
Summary: Using the DattoRMM API to export all Sites to a CSV file.
---

<img src="{attach}dattormm.png"  width="33%" height="33%">

What began as a task just to [export all Sites from a DatoRMM instance to a CSV file](https://github.com/jscooksey/DattoRMM-Site-Export), has started me down the path of building a module to deal with many of the DattoRMM API end points. 

Mainly working around the REST APIs that I needed to use to perform certain tasks, I've begun refactoring the export code to become more of an API interface module which may grow to be more useful.  Other tasks may take my time away from this, but I will see were it may go.

The original code to export of sites is here [DattoRMM-Site-Export](https://github.com/jscooksey/DattoRMM-Site-Export).  Currently this code pulls all Sites from a [DattoRMM](https://www.datto.com/au/products/rmm/) environment and exports the basic details in to CSV format file.  It removes the system sites called Managed, OnDemand & Deleted Devices, so that you only get an export of the customer base.

Also in the repo is code to set Site variables in DattoRMM sites read in from a csv, as this was part of the next steps I needed to take.

Gets the API URL, Key and Secret from .env or environment variables (example below)

Functions to interact with the DattoRMM API are in the [dattormmapi.py](https://github.com/jscooksey/DattoRMM-Site-Export/blob/main/dattormmapi.py) Python file.

Main function to do the API requests and export to CSV is in the [export_sites.py](https://github.com/jscooksey/DattoRMM-Site-Export/blob/main/export_sites.py) Python file.

Refactoring to make this a more versatile module to handle interactions with the DattoRMM API will go in to a new GitHub repo, which I'll make public once its formed up some more. 
