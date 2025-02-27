---
Title: Pelican Static Site Generator
Date: 2023-06-18 20:33
Status: published
Category: Code
Tags: Python, Code, Frontend, Web, Pelican
Keywords: Python, Code, Frontend, Web, Pelican
Slug: pelican-static-site-generator
Author: Justin Cooksey
Image: pelican.png
Description: Using Pelican for statc site generation to replicate site created in GatsbyJS
---

<a href="https://getpelican.com/"><img src="{attach}pelican.png"  width="33%" height="33%"></a>

I've been investigating [Pelican a static site generator](https://getpelican.com/) to replace my current [GatsbyJS](https://www.gatsbyjs.com/) generated site.  Im far more at home and familiar with [Python](https://www.python.org/) and [Jinja2](https://palletsprojects.com/p/jinja/), so that was part of my reasoning for taking a look in to it.

So working along the basis of replacing my current GatsbyJS created site and posts with one created by Pelican, the following cover my initial issues and solutions.  I've only added brief notes on what was done, without going in to detail as the plugin sites cover correct use in detail.


[TOC]


## Redirect old site paths

In investigting moving to a new static site gernerator I also decided to change the sturcure a little. Since not many articles existed at the time of this posting minimal redirects will have to be created.  

So how does Pelican handle this on a per article basis? 

Enter the [pelican-redirect](https://github.com/slinkp/pelican-redirect) plugin.  Installing it is as simple as installling from PyPi 
```bash
pip install pelican-redirect
```
Then by adding an additional line in to the metadata of each post
```yaml
original_url: blog/hacktoberfest-2019.html
```
Pelican will create an HTML file at the URL location specified that will redirect to the new post  location that it will create.

## Canonical 

In order to add the canonical header entry on articles using the **SITEURL** variable does not create what you need if **RELATIVE_URL = True** is set.  To get around this and always use a full URL you can copy the **SITEURL** variable in to **CANONICALURL** and then use that variable in the **base.html** template.

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

## Sitemap

To produce [sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview) files for SEO add the [pelican-sitemap](https://github.com/pelican-plugins/sitemap) plugin:
```bash
pip install pelican-sitemap
```
and then adding a **SITEMAP** variable to the **pelicanconf.py** as described in the README of the Repo


## Social Media Shares

I also had on my curent site social media sharing links at the bottom of every article, allowing the reader to share the article on there own social media streams. 

The [share-post](https://github.com/pelican-plugins/) plugin does this and again is simply installed using pip
```bash
pip install pelican-share-post
```
Then in the article.html template add link to atricle.share_post attribute

```html
<a href="{{article.share_post\['twitter'\]}}">...</a>
<a href="{{article.share_post\['facebook'\]}}">...</a>
<a href="{{article.share_post\['linkedin'\]}}">...</a>
```

## RSS/Atom Feed

[Adding in Atom (or RSS) feeds](https://docs.getpelican.com/en/latest/settings.html#feed-settings) is as easy as changing a few options, as this is built in to Pelcon.  Changing a few options in the **pelicanconf.py** 

```python
FEED_MAX_ITEMS = 20
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
```

## Code Highlighting

Markdown code highlighting is processed ultimately through Pygment which can be personailsed but has some builtin styles.  Examples are on the Pygment site [here](https://pygments.org/styles/#) and css files for these can be copied from the repo [richleland/pygments-css](https://github.com/richleland/pygments-css).

You can copy the CSS file of your choice to your themes static folder (eg **static/css/pygment.css**) and then import that in the **base.html**  

```html
@import url(pygment.css);
```

Markdown code blocks can then be used and [refer to the type of code](https://www.markdownguide.org/extended-syntax/#syntax-highlighting) inside them.

## Conclusion

This is as far as I've gotten so far in working in Pelican and this Pelican created site is initially hosted on [GitHub Pages](https://pages.github.com/) at the URL [https://jscooksey.github.io/Pelican/](https://jscooksey.github.io/Pelican/)

I'll as I figure things out further, with the intention this will replace the primary site hosted at my domain.
