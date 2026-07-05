
<a id='changelog-2026.07.05'></a>
# 2026.07.05 — 2026-07-05

## Changed

- Upgrading all packages to latest
- Work on imrpving image processing throughout


# 2026-01-31

## Changed

- Upgraded packages
- Changed font to be mixed case and removed character spacing. Now need to adjust some sizes, but better

# 2026-01-04

## Removed

- Removed netlify config file, as now hosted on cloudlfare

# 2026-01-04

## Changed

- Changed main.css for main::before for menu to use f0c9 which is the bars for a menu

# 2026-01-04

## Changed

- Setup Jinja2 macro file macros.html in templates
  - Using this macro in index.html, tag.html & category.html

# 2026-01-04

## Changed

- Changed tag.html and category.html templates to not use index which was doubling up canonical meta data
- Will need to pull out the list and use in function as it is in use in 3 different templates, tag, catgeroy & index

# 2026-01-04

## Added

- Started using UV for package management.  Testing this still
- Created requirements.txt output from UV
- Upgraded all packages to latest
- Upgraded to using Pelican Image Process module, and updated content files

# 2025-05-21

## Added

- Added pygment.css to get code block color highlites

# 2025-05-21

## Changed

- Fixed avatar link to point to /about rather than #

# 2025-05-21

## Changed

- Changed Avatar image

# 2025-05-20

## Changed

- Changed to FontAwesome Free 6
  - Now allows for Bluesky icon in Articles
  - Fixes Issue #3

# 2025-05-19

## Changed

- Upgraded to Python 3.13.3 after confirming Netlify support
  - Updated netlify.toml to use this version
  - updated .pyth-version to use it locally
- Upgraded to Pelcian 4.11.0
  - Upgraded Pelican modules post this
  - Upgraded allpackages to support new Python and Pelican

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
