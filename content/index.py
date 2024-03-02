config = {
    "template": "index.html",
    "title": "Your Name | Architect",
    "content": """ [% markdown
    [Projects](projects)  |  [About]([% link /about.py %])  |  [Contact]([% link /contact.py %])
    %]
    """,
}
