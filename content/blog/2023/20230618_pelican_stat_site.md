Title: Pelican Static Site Generator
Date: 2023-06-18 20:33
Category: Article
Tags: Python, Code, Frontend
Slug: pelican-static-site-generator
Author: Justin Cooksey
Image: pelican.png
Summary: Using Pelican for statc site generation to replicate site created in GatsbyJS

<img src="{attach}pelican.png"  width="33%" height="33%">

[Pelican](https://docs.getpelican.com/en/latest/#) is a static site generator written in Python

## Redirect for old sites paths

In investigting moving to a new static site gernerator I also decided to chnage the sturcure since not many articles existed at thi time.
So I needed a redirect if someone used the original link to the new link being used

Enter the [pelican-redirect](https://github.com/slinkp/pelican-redirect) plugin.  Adding an additional line in to the metadata ```original_url: blog/hacktoberfest-2019.html``` created an HTML file at the URL that would redirect to the new location.

## Social Media Shares

I also wanted to have social media sharing links at the bottom of every aarticle.  This is when I brought in the [share-post](https://github.com/pelican-plugins/) plugin.

## Canonical 

In order to add the canonical header entry on articles using the ```SITEURL``` variable does not create what you need if ```RELATIVE_URL = True``` is set.  To get around this and always use a full URL you can copy the ```SITEURL``` variable in to ```CANONICALURL``` and then use that variable in the **base.html** template.

**pelicanconf.py**
```python
SITEURL = "https://jscooksey.github.io/Pelican"
CANONICALURL = SITEURL
```

**base.html**
```html
<head>
  <title>{{SITENAME}}</title>
  {% if article %}
    <link rel="canonical" href="{{ CANONICALURL }}/{{ article.url }}" />
  {% endif%}
```