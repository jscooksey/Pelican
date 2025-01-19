---
Title: Development on Fedora 41
Date: 2025-01-19 16:00
Status: draft
Category: Code
Tags: Python, Code, Linux, Fedora
Keywords: Python, Code, Linux, Fedora, Fedora 41
Slug: 2025-01-19-development-on-fedora-41
Author: Justin Cooksey
Summary: Moving to Fedora (41) for my primary development platform.  The initial migration.
---


<img src="{attach}fedora_ss.png"  width="33%" height="33%">

**Finally made the change**

Came with Python 3.13.1

VSCode

Getting pyenv working to allow using different version of Python

```bash
sudo dnf install @development-tools
sudo dnf install python3-tkinter python3-xlib
sudo dnf install bzip2-devel ncurses-devel libffi-devel readline-devel tk-devel libsqlite3x-devel

```
https://docs.fedoraproject.org/en-US/project/_images/banner-getfedora_sq.png