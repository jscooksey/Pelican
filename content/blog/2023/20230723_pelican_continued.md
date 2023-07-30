---
Title: Publishing Pelican Created Site
Date: 2023-07-23 21:33
Status: draft
Category: Code
Tags: Python, Code, Frontend, Web, Pelican, Netlify
Keywords: Python, Code, Frontend, Web, Pelican, Netlify, publish
Slug: pelican-created-site
Author: Justin Cooksey
Image: pelican.png
Summary: A continuation of moving a simple static built site to the Pelican Static Site geenrator to get it pulished on Netlify
---

<a href="https://getpelican.com/"><img src="{attach}pelican.png"  width="33%" height="33%"></a>

This is the second part ([Part 1](https://justincooksey.com/boog/2023/pelican-static-site-generator)) of my migrating a static web site over to [Pelican Static Site Generator](https://docs.getpelican.com/en/latest/index.html), after my inital posting Pelican Static Site Generator

## Google Analytics

To trasnfer over my Google Analytics web site code to the Pelican created site was as simple as adding it in to pelicanconf.py as a varible and done.  This is all well docmented on the site

## Hosting and Replcaing on Netlify

Make sure you have requirements.txt file
Make sure pelicanconf.py and publishconf.py are up to date (especially URL)
   pelican content -s publishconf.py
   output
Associte repository
Setting up Netlify
Pyuthon 3.8 only
netlify.toml to handle 404


