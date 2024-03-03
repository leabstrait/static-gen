config = {
    "template": "landing.j2",
    "title": "Your Name | Architect",
    "content": """ [% md
    [Projects](projects)  |  [About]([% pylink /about.py %])  |  [Contact]([% pylink /contact.py %])
    %]
    """,
}
