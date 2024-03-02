import os
import shutil
import markdown
from jinja2 import Environment, FileSystemLoader
import importlib.util
import textwrap
import re

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
    "default_template": "base.html",
    "baseURL": "https://example.com",
    "languageCode": "en-us",
    "title": "My Website",
    "description": "This is my website",
    "author": "Your Name",
    "keywords": "website, blog, portfolio",
    "copyright": "© Your Name",
    "menu": [
        {"name": "Your Name", "url": "[% link / %]"},
        {"name": "Projects", "url": "[% link /projects %]"},
        {"name": "About", "url": "[% link /about.py %]"},
        {"name": "Contact", "url": "[% link /contact.py %]"},
    ],
    "social": {
        "twitter": "username",
        "github": "username",
        "linkedin": "username",
        "email": "username@example.com",
    },
}


# Load templates
env = Environment(loader=FileSystemLoader(config["directories"]["template"]))


# Function to preprocess strings in the config with shortcodes
def preprocess_config(config, base_path=""):
    # Define the shortcode patterns and their corresponding functions
    shortcode_patterns = {
        r"\[\%\s*year\s+\%\]": lambda: "2024",  # Example shortcode for current year
        r"\[\%\s*link\s+([\s\S]+?)\s*\%\]": lambda match: get_link_target(
            match.group(1)
        ),
        r"\[\%\s*markdown\n+([\s\S]+?)\s*\%\]": lambda match: convert_markdown_to_html(
            match.group(1)
        ),
        r"\[\%\s*markdownpath\s+([\s\S]+?)\s*\%\]": lambda match: convert_markdownpath_to_html(
            os.path.join(base_path, match.group(1))
        ),
        # Add more shortcode patterns and their corresponding functions as needed
    }

    # Function to replace shortcodes in a string
    def replace_shortcodes(string):
        # Iterate through each shortcode pattern
        for pattern, shortcode_func in shortcode_patterns.items():
            # Replace the shortcode with its corresponding value
            string = re.sub(pattern, lambda match: shortcode_func(match), string)
        return string

    # Iterate through each key-value pair in the config
    for key, value in config.items():
        # If the value is a string, preprocess it
        if isinstance(value, str):
            config[key] = replace_shortcodes(value)
        # If the value is a dictionary, recursively preprocess it
        elif isinstance(value, dict):
            preprocess_config(value, base_path=base_path)
        # If the value is a list, preprocess each element
        elif isinstance(value, list):
            config[key] = [
                (
                    replace_shortcodes(item)
                    if isinstance(item, str)
                    else preprocess_config(item, base_path=base_path)
                )
                for item in value
            ]
    return config


# Function to get link target based on input
def get_link_target(input):
    # Example logic to determine link target based on input
    return input.replace("py", "html")


# Function to convert Markdown string to HTML
def convert_markdown_to_html(markdown_content):
    return markdown.markdown(textwrap.dedent(markdown_content))


# Function to convert Markdown file to HTML
def convert_markdownpath_to_html(markdown_path):
    with open(markdown_path, "r") as f:
        markdown_content = f.read()
        return convert_markdown_to_html(markdown_content)


# Function to copy assets while preserving directory structure
def copy_assets(source_dir, destination_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if not (file.endswith(".py") or file.endswith(".md")):
                source_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_path, source_dir)
                destination_path = os.path.join(destination_dir, relative_path)
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copyfile(source_path, destination_path)


# Function to process each content file
def process_content(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if not filename.endswith(".py"):
                continue

            content_path = os.path.join(root, filename)

            # Load the content module dynamically
            module_name = os.path.splitext(filename)[0]
            spec = importlib.util.spec_from_file_location(module_name, content_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Preprocess content config
            processed_content_config = preprocess_config(module.config, base_path=root)

            # Get template name and remove it from processed content config
            template_name = processed_content_config.pop(
                "template", config["default_template"]
            )

            # Load template
            template = env.get_template(template_name)

            # Render HTML content passing in config and processed_content_config
            rendered_content = template.render(
                **{
                    key: value
                    for key, value in config.items()
                    if key not in processed_content_config.keys()
                },
                **processed_content_config,
            )

            # Compute relative path of content file within content directory
            rel_path = os.path.relpath(content_path, config["directories"]["content"])
            # Construct output path
            output_path = os.path.join(
                config["directories"]["output"], rel_path.replace(".py", ".html")
            )

            # Ensure directory structure exists in the output directory
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            # Write rendered content to output file
            with open(output_path, "w") as f:
                f.write(rendered_content)


# Process content files
config = preprocess_config(config, base_path="")
process_content(config["directories"]["content"])

# Copy assets to output directory
copy_assets(
    config["directories"]["script"],
    os.path.join(config["directories"]["output"], "scripts"),
)
copy_assets(
    config["directories"]["style"],
    os.path.join(config["directories"]["output"], "styles"),
)
copy_assets(
    config["directories"]["media"],
    os.path.join(config["directories"]["output"], "media"),
)
copy_assets(
    config["directories"]["content"],
    config["directories"]["output"],
)

print(
    f"Static site generated successfully! Output in {config['directories']['output']}"
)
