
# 2025-03-16

## Changed

- Changed to buttons on pagination

# 2025-03-13

## Added

- Pagination on index page and others.  Looking to expand that later

## Changed

- Authors pages are not created AUTHOR_SAVE_AS = None
  - Using the ABout page only for this

# 2023-08-07

## Added

- With Google Analytics 4 in use now, added chnages and confirmed and then updated the markdown for the blog post on the same.

-->

# 2023-07-30

## Added

- Google Analytics code in to pelicanconf.py

## Changed

- Modifed the About page to be much the same as the GitHub profile
- Changed the logo image to the seal/crest

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
