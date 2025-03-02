---
Title: Publishing Pelican Created Site
Date: 2023-07-30 19:30
Status: published
Category: Code
Tags: Python, Code, Frontend, Web, Pelican, Netlify
Keywords: Python, Code, Frontend, Web, Pelican, Netlify, publish
Slug: pelican-created-site
Author: Justin Cooksey
Image: pelican.png
Description: A continuation of moving a simple static built site to the Pelican Static Site geenrator to get it pulished on Netlify
---

<a href="https://getpelican.com/"><img src="{attach}pelican.png"  width="33%" height="33%"></a>

This is the second part ([see part 1 here](https://justincooksey.com/blog/2023/pelican-static-site-generator.html)) of my migrating a static web site over to [Pelican Static Site Generator](https://docs.getpelican.com/en/latest/index.html), after my inital posting Pelican Static Site Generator

## Google Analytics



To transfer over [Google Analytics](https://developers.google.com/analytics/devguides/collection) web site code to the Pelican created site was as simple as adding it in to pelicanconf.py as a varible and done.  
<sup><sub>Amended 2023-08-07</sub></sup>
With Googles GA-4 a different approach was taken.  I added a new varible to hold the GA4 code:

**pelicanconf.py**
```python
GOOGLE_GA4_ID = your_site_code
```
Then in the **base.html** template I added the Google supplied HTML code in the **head** section, with the Jinja2 varible pulled from **pelicanconf.py**:

```html
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={{ GOOGLE_GA4_ID }}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', '{{ GOOGLE_GA4_ID }}');
    </script>
    <!-- Google tag (gtag.js) -->
  </head>
```

## Hosting and Replacing on Netlify

As the GatsbyJS site was hosted on Netlify which also supports Python and Pelican builds rehosting on Netlify was relatively easy.

First though was getting the source repository ready.  Starting with making sure the requirements.txt file exists, as Netfliy build process will be using this to install the required python libraries for the site.  I generally keep this up to date as I work, but simply creating it again with the usual command is easy enough:

```bash
pip freeze > requirements.txt
```

Then making sure the **publishconf.py** file has all the correct settings for the final published site.  This was pretty much correct and needed only confirming that it had the correct variables in it for the final site.  Overwriting the development variables stored in **pelicanconf.py**. 

A **netfliy.toml** file in the root of the repo will give Netlify the commands to build the site and location of the built site files to publish:

```toml
[build]
command = "pelican content -s publishconf.py"
publish = "output"
```

also a block to specificy the page (HTML file) to display for a 404 page not found repsonse:
 
```toml
[[redirects]]
from = "/*"
to = "/404.html"
status = 404
```

## Linking in the new repo

After those things are all settled it is just a matter of [linking the GitHub repo to the the Netlify site](https://docs.netlify.com/configure-builds/repo-permissions-linking/), and Netfliy will do the rest.  Building the site and publishing it ready for use.

## So is that it?

Well, while I have the Pelican built site now the active builder for the static pages on the site, I still have plenty to work on.  Plenty to upgrade including the theme, which is still not quite right, and of course content on the site for other projects and well whatever else is happening in life......


