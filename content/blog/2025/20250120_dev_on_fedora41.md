---
Title: Development on Fedora 41
Date: 2025-01-20 16:00
Status: published
Category: Code
Tags: Python, Code, Linux, Fedora
Keywords: Python, Code, Linux, Fedora, Fedora 41, pyenv
Slug: 2025-01-20-development-on-fedora-41
Author: Justin Cooksey
Image: fedora_ss.png
Description: Moving to Fedora (41) for my primary development platform.  The initial migration.
---


<img src="{attach}fedora_ss.png"  width="33%" height="33%">

## So, moving to Linux ...

I've been using MacOS for a few years now for my own development environment, and always enjoyed using something different from the required work Windows systems.  MacOS, and Apple hardware, have always been pretty on point in my oppinion.  However, for a while now, I'd wanted to jump back in to Linux as my primary OS. I have already been moving away from commercial applications, getting rid of my Adobe account and migrating to using [Darktable](https://www.darktable.org/) along with other subscription based applications (not all). This is my inital experience migrating from developing on Windows and MacOS to developing on Linux, or in particular [Fedora](https://fedoraproject.org/) 41.

Most of my development work is in [Python](https://www.python.org/), although work means I do a fair share of PowerShell, so the initial focus is around [Python](https://www.python.org/) and getting my normal tools up and running.

## [Visual Studio Code](https://code.visualstudio.com/)

[Visual Studio Code](https://code.visualstudio.com/) (VSCode) does come as a FlatPak via the Software app in [Fedora](https://fedoraproject.org/) 41, and its a pretty recent version (as of time of writting) at 1.96.1 with the latest being 1.96.4.  However I opted to install directly off the VSCode web site and use the [rpm download](https://code.visualstudio.com/Download).  This installed without any 
issues and the [Fedora](https://fedoraproject.org/) Software app does show it as installed after using this method.  I had no issues at all on first run and syning in the Extenxsion I use by sing Setting Sync to replicate what I have on my MacOS machine.

## Shell

I haven't yet explored and/or moved to [ZSH](https://www.zsh.org/) at this time.  I know that along with [Oh My Zsh](https://ohmyz.sh/) it makes for a pretty useful Shell, but at this point I'm sticking with the default [bash](https://www.gnu.org/software/bash/) and will look at options little later on.

## [Python](https://www.python.org/)

Fedora 41 came with [Python](https://www.python.org/) 3.13.1, which at the time of writing is the latest release version of [Python](https://www.python.org/).  Sometimes though we need to be able to run our code against other, older versions of [Python](https://www.python.org/).  Enter [pyenv](https://github.com/pyenv/pyenv) ...

#### [pyenv](https://github.com/pyenv/pyenv)

If you havent used [pyenv](https://github.com/pyenv/pyenv) before the [Real Python](https://realpython.com/) site has a great article on [Managing Multiple Python Versions With pyenv](https://realpython.com/intro-to-pyenv/)

[pyenv](https://github.com/pyenv/pyenv) took a little bit longer to get operational.  This was because the default install of [Fedora](https://fedoraproject.org/) 41 does not install development packages, so I had to do a little research and test and research again before I got it all working.  First off was to install the development-tools group of packages after which I still had some missing libraries to add in as well.  The final result is as follows:

```bash
sudo dnf install @development-tools
sudo dnf install python3-tkinter python3-xlib bzip2-devel ncurses-devel libffi-devel readline-devel tk-devel libsqlite3x-devel
```

This has now allowed me to install and use other versions of Python on my [Fedora](https://fedoraproject.org/) 41 based laptop.  Which means I can now update this web site with this article ...

