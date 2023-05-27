AUTHOR = "Justin Cooksey"
SITENAME = "Justin Cooksey Pelican Test"
SITESUBTITLE = "Thoughts and Code by Justin Cooksey"
SITEURL = "https://jscooksey.github.io/Pelican"

# THEME = "notmyidea"
THEME = "future-imperfect"

PATH = "content"
ARTICLE_PATHS = ["blog"]
ARTICLE_SAVE_AS = "{date:%Y}/{slug}.html"
ARTICLE_URL = "{date:%Y}/{slug}.html"

TIMEZONE = "Australia/Sydney"

DEFAULT_LANG = "en"

RELATIVE_URLS = True

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
    ("Another social link", "#"),
)

CONTACTS = (
    ("Twitter", "fa-twitter", "https://twitter.com/jscooksey"),
    ("DEV", "fa-dev", "https://facebook.com/theanalogfox"),
    ("Mastodon", "fa-mastodon", "https://www.instagram.com/theanalogfox/"),
    ("GitHub", "fa-github", "info@theanalogfox.com"),
)

DEFAULT_PAGINATION = 3
