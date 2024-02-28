**YAML-MD Static Site Generator**

**Description:**
The YAML-MD Static Site Generator is a Python script for creating static websites from YAML and Markdown files. It converts YAML files with metadata and Markdown content into HTML pages, using Jinja2 templates for customization. The included example is for an Architecture Portfolio website and can be modified according to requirements.

**Features:**
- Convert YAML and Markdown to HTML.
- Jinja2 templating for customization.
- Asset management for scripts, stylesheets, and media files.

**Usage:**
1. Place content in YAML files with metadata and Markdown.
   1. In YAML markdown content can be specified as a text value inside ` ```markdown ` and ` ``` `, or just give a relative path to the markdown file in `*.md` format.
   2. The script will process the markdown to HTML before passing it to the template.
2. Define templates using Jinja2 syntax.
3. Run the generator script to build the site.
4. Access the generated site in the output(default `docs`) directory.

**Installation:**
1. Clone/download the repository.
2. Install dependencies from `requirements.txt`.
3. Customize content, templates, and assets.
4. Run the generator script ```python genereate.py```
