AUTHOR = "Justin Cooksey"
SITENAME = "Justin Cooksey Codes"
SITESUBTITLE = "Thoughts and Code by Justin Cooksey"
SITEURL = "https://jscooksey.github.io/Pelican"

THEME = "jsctheme"

PATH = "content"
ARTICLE_PATHS = ["blog"]
ARTICLE_SAVE_AS = "{date:%Y}/{slug}.html"
ARTICLE_URL = "{date:%Y}/{slug}.html"

TIMEZONE = "Australia/Sydney"

DEFAULT_LANG = "en"

RELATIVE_URLS = True

STATIC_PATHS = [
    "extra",
]

EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    ("Twitter", "https://twitter.com/jscooksey"),
    ("GitHub", "https://github.com/jscooksey"),
)

CONTACTS = (
    ("Twitter", "fa-twitter", "https://twitter.com/jscooksey"),
    ("DEV", "fa-dev", "https://dev.to/jscooksey"),
    ("Mastodon", "fa-mastodon", "https://fosstodon.org/@jscooksey"),
    ("GitHub", "fa-github", "https://github.com/jscooksey"),
)

DEFAULT_PAGINATION = 3
