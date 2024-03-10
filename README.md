## `staticgen`<div align="right">[![Tests](https://github.com/leabstrait/staticgen/actions/workflows/tests.yml/badge.svg)](https://github.com/leabstrait/staticgen/actions/workflows/tests.yml)</div>

`staticgen` simplifies static site generation from Markdown content and Jinja2 templates.

## Installation and Upgrade

```bash
pip install git+https://github.com/leabstrait/staticgen
```

## Usage

### Initialize Your Project:

-   Create a new project directory.
-   Navigate into it.
-   Initialize a starter project with predefined structure and configuration:
    ```bash
    staticgen init
    ```

### Configure Your Website:

-   Create a `config.py` file in the project root.
-   Customize settings.

### Prepare Content Files:

-   Use Markdown files with a `.py` extension.
-   Include metadata and content.

### Customize Templates:

-   Customize `base.html` or add more templates.

### Generate Your Site:

```
staticgen gen
```

-   Output in `docs` directory.

### Preview Your Site:

-   Start a local HTTP server:
    ```
    cd docs
    python -m http.server
    ```
-   Open `http://localhost:8000`.

## Customization

-   Extend `staticgen` or edit generated files.
-   Customize CSS and JS.

## License

This project is dedicated to the public domain under the [Unlicense](UNLICENSE).
