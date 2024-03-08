# Static Site Generator

## `staticgen` [![Tests](https://github.com/leabstrait/static-gen/actions/workflows/tests.yml/badge.svg)](https://github.com/leabstrait/static-gen/actions/workflows/tests.yml)

This is a Python package for generating static websites from Markdown content and Jinja2 templates.

## Installation

You can install the `staticgen` package directly from GitHub using `pip`:

```
pip install git+https://github.com/leabstrait/static-gen
```

## Usage

1. **Initialize Your Project**: To start using the static site generator, you'll need to set up a new project directory. Follow these steps:

   - Create a new directory for your static site project.
   - Navigate into the newly created directory.

2. **Configure Your Website**: After setting up your project directory, you need to configure your website by creating a configuration file named `config.py`. Here's what you should do:

   - Create a new Python file named `config.py` in the root directory of your project.
   - Customize your website configuration in this file according to your preferences. You can use the provided example as a template. The configuration includes settings such as directories, templates, default values, menu items, social links, etc.

3. **Prepare Content Files**: The content of your website will be stored in Markdown files, which should be converted to HTML during the site generation process. Follow these guidelines for preparing your content files:

   - Create Markdown content files with a `.py` extension. These files should follow a specific structure specified in the examples provided.
   - Each content file should contain metadata and Markdown content. The metadata typically includes information such as title, date, author, etc., and is specified using Python dictionaries.
   - Ensure that the metadata and Markdown content are properly formatted within each content file.

4. **Customize Templates**: Customize your Jinja2 templates to define the layout and structure of your website. The default template provided is `base.html`, but you can create additional templates as needed. Templates allow you to define the overall look and feel of your site, including headers, footers, navigation menus, etc.

5. **Generate Your Site**: Once your project is set up and configured, you can generate your static site by running the following command in your terminal:

   ```
   staticgen
   ```

   This command will trigger the site generation process based on the configuration and content you provided. The generated site will be placed in a directory named `docs` within your project directory.

6. **Preview Your Site**: After generating your site, you can preview it locally by serving the static files using a simple HTTP server. Here's how:

   - Navigate into the `docs` directory within your project.
   - Start a local HTTP server using Python's built-in HTTP server:

     ```
     cd docs
     python -m http.server
     ```

   - Open your web browser and navigate to `http://localhost:8000` to view your site.

## Customization

- To add additional functionality or modify existing behavior, you can extend the `staticgen` package or edit the generated files directly.
- You can also customize the CSS styles and JavaScript scripts in their respective directories within your project.

## License

This project is dedicated to the public domain under the [Unlicense](UNLICENSE).
