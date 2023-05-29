Title: Datto RMM API Sites Export
Date: 2023-05-29 12:30
Category: Article
Tags: Python, Code, RMM, DattoRMM
Slug: 2023-dattormm-api
Author: Justin Cooksey
Summary: Using the DattoRMM API to export all Sites to a CSV file.

![DattoRMM]({attach}dattormm.png)

Using the DattoRMM API to export all Sites to a CSV file
[GitHub Repo](https://github.com/jscooksey/DattoRMM-API)

Pulls all Sites from a [DattoRMM](https://www.datto.com/au/products/rmm/) environment and export basic details in to CSV formatted file.
Removes the system sites of Managed, OnDemand & Deleted Devices.

Gets the API URL, Key and Secret from .env or environment variables (example below)

Functions to interact with the DattoRMM API are in the [dattormmapi.py](https://github.com/jscooksey/DattoRMM-API/blob/main/dattormmapi.py) Python file.

Main function to do the API requests and export to CSV is in the [export_sites.py](https://github.com/jscooksey/DattoRMM-API/blob/main/export_sites.py) Python file.

Not much error/exception managment in this at the moment.
