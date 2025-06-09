AUTHOR = "Justin Cooksey"
SITENAME = "Justin Cooksey Codes"
SITESUBTITLE = "Thoughts and Code by Justin Cooksey"
SITEURL = "https://justincooksey.com"
CANONICALURL = SITEURL

DELETE_OUTPUT_DIRECTORY = True

GOOGLE_GA4_ID = "G-M6K7S460VR"

# THEME = "themes/simple"
THEME = "themes/future-imperfect"

PATH = "content"
ARTICLE_PATHS = ["blog"]
ARTICLE_SAVE_AS = "blog/{date:%Y}/{slug}.html"
ARTICLE_URL = "blog/{date:%Y}/{slug}.html"

AUTHOR_SAVE_AS = None

PAGE_PATH = ["pages"]
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

TIMEZONE = "Australia/Sydney"

DEFAULT_LANG = "en"

RELATIVE_URLS = True

SUMMARY_MAX_LENGTH = 50
SUMMARY_END_SUFFIX = "..."

STATIC_PATHS = [
    "extra",
]

EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

# Feed generation is usually not desired when developing
FEED_MAX_ITEMS = 20
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    "extension_configs": {
        # Needed for code syntax highlighting
        "markdown.extensions.codehilite": {"css_class": "highlight", },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {"title": "Table of Contents"},
    },
    "output_format": "html5",
}

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Menu Bar Headlines
HEADLINES = (
    ("Code", "/category/code.html"),
    ("Network DevOps", "/category/network-devops.html"),
    ("About", "/about"),
)

# Social widget
SOCIAL = (
    ("Bluesky", "https://bsky.app/profile/jscooksey.bsky.social"),
    ("DEV", "https://dev.to/jscooksey"),
    ("Mastodon", "https://fosstodon.org/@jscooksey"),
    ("GitHub", "https://github.com/jscooksey"),
    ("LinkedIn", "https://www.linkedin.com/in/jscooksey/"),
)

CONTACTS = (
    ("Bluesky", "fa-html5", "https://bsky.app/profile/jscooksey.bsky.social"),
    ("DEV", "fa-dev", "https://dev.to/jscooksey"),
    ("Mastodon", "fa-mastodon", "https://fosstodon.org/@jscooksey"),
    ("GitHub", "fa-github", "https://github.com/jscooksey"),
    ("LinkedIn", "fa-linkedin", "https://www.linkedin.com/in/jscooksey/"),
)

DEFAULT_PAGINATION = 6
DEFAULT_ORPHANS = 0

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
    "exclude": [],
}

TAG_URL = "tags/{slug}.html"
TAG_SAVE_AS = "tags/{slug}.html"

IMAGE_PROCESS = {
    "crisp": {
        "type": "responsive-image",
        "srcset": [
            ("1x", ["scale_in 800 600 True"]),
            ("2x", ["scale_in 1600 1200 True"]),
            ("4x", ["scale_in 3200 2400 True"]),
        ],
        "default": "1x",
    },
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 718px, "
            "100vw"
        ),
        "srcset": [
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "800w",
    },
}