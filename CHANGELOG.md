
# 2023-07-23

## Changed

- *latest_posts.html* Jinja2 template file so it now calculaets the path to the image file while iterating over articles

# 2023-07-16

## Added

- pygment.css file to get code fromatting correctly created
    - Taken from https://github.com/richleland/pygments-css/tree/master  monokai.css

# 2023-07-16

## Added

- Added table of contents option after reviewing site
   https://cloudbytes.dev/snippets/add-a-table-of-contents-using-markdown-in-pelican

# 2023-06-19

## Added

- Sitemap create plugin with [pelican-sitemap](https://github.com/pelican-plugins/sitemap)

- Added RSS feed beginings with adding FEED variable in **pelicanconf.py**
  - Need to confirm creation to match previsou site

# v0.1.1 -- 2023-06-18

## Added

- Share Post Pelican plugin to allow social media share links/icons at the bottom of an article [share-post plugin](https://github.com/pelican-plugins/share-post)
- Modified aritcle.html to use icons for the sharing links

- Pelican Redirect plugin to rediect old URLs from previous blog to ordered by year paths in use. [pelican-redirect](https://github.com/slinkp/pelican-redirect)

## Changed

- Setup to add canonical tag for articles
  - CANONICALURL variable in **pelicanconf.py** duplicating SITEURL.  This was added to ensure full URL used in ref in case of **RELATIVE_URL** being true.
  - base.html change to include the **rel="canonical"** if this its an article using the CANONICALURL variable

# v0.1.0 -- 2023-06-13

## Added

- scriv added to maintain the changelog. See [nedbat/scriv](https://github.com/nedbat/scriv)
- Begining of CHANGELOG.md
