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

I've been using MacOS for a few years now for my own development environment, and always enjoyed using something different for the required work Windows OS.  MacOS and Apple hardweare have always been pretty on point in my oppinion.  But for a while now I'd wanted to jump back in to Linux as my primary OS, and move away from the commercial. I was also already moving away from the commercial applications as well, getting rid of my Adobe account and migrating to using Darktable along with the utter being disuaded by the constant link between what im Searching (Google and Chrome), what I see in my social media stream, and what others near me also see in there social media stream.  Anyway this is more on the what I found moving from my experience with developing on Windows and MacOS to developing on Linux, or in particular Fedora 41

Most of my development work is in Python, although work means I do a fair share of PowerShell, so the initial focus is around Python and getting my normal tools up and running

#### [Visual Studio Code](https://code.visualstudio.com/)

[Visual Studio Code](https://code.visualstudio.com/) does come as a FlatPak via the Software app in Fedora 41, and its a pretty recent version (as of time of writting) at 1.96.1 with the latest being 1.96.4.  However I opted to sinatll directly off the VS Code web site and use the rpm download.  This installed without any 
issues and the Fedora Software app does show it as installed after using this method.  I had no issues at all on first run and syning in the Extenxsion I use by sing Setting Sync to replicate what I have on my MacOS machine.

I havent yet explored and/or moved to [ZSH](https://www.zsh.org/) at this time.  I know it along with [Oh My Zsh](https://ohmyz.sh/) make for a pretty useful Shel, but at this point I'm sticking with the default and will look ath that a litte later on.


Came with [Python](https://www.python.org/) 3.13.1


Getting [pyenv](https://github.com/pyenv/pyenv) working to allow using different version of Python
The [Real Python](https://realpython.com/) site has a great article on [Managing Multiple Python Versions With pyenv](https://realpython.com/intro-to-pyenv/)

```bash
sudo dnf install @development-tools
sudo dnf install python3-tkinter python3-xlib
sudo dnf install bzip2-devel ncurses-devel libffi-devel readline-devel tk-devel libsqlite3x-devel

```
https://docs.fedoraproject.org/en-US/project/_images/banner-getfedora_sq.png