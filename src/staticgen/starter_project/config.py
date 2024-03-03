# Define configuration as Python data structure
config = {
    "directories": {
        "content": "content",
        "template": "templates",
        "script": "scripts",
        "style": "styles",
        "media": "media",
        "output": "docs",
    },
    "default_template": "base.j2",
    "baseURL": "https://example.com",
    "languageCode": "en-us",
    "title": "My Website",
    "description": "This is my website",
    "author": "Your Name",
    "keywords": "website, blog, portfolio",
    "copyright": "© Your Name",
    "menu": [
        {"name": "Your Name", "url": "[% pylink / %]"},
        {"name": "Projects", "url": "[% pylink /projects %]"},
        {"name": "About", "url": "[% pylink /about.py %]"},
        {"name": "Contact", "url": "[% pylink /contact.py %]"},
    ],
    "social": {
        "twitter": "username",
        "github": "username",
        "linkedin": "username",
        "email": "username@example.com",
    },
}
