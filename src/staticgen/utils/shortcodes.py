import os
import re
import markdown
import textwrap

# Function to preprocess strings in the config with shortcodes
def preprocess_config(cfg, base_path=""):
    # Define the shortcode patterns and their corresponding functions
    shortcode_patterns = {
        r"\[\%\s*year\s+\%\]": lambda: "2024",  # Example shortcode for current year
        r"\[\%\s*pylink\s+([\s\S]+?)\s*\%\]": lambda match: get_link_target(match.group(1)),
        r"\[\%\s*md\n+([\s\S]+?)\s*\%\]": lambda match: convert_md_to_html(match.group(1)),
        r"\[\%\s*mdpath\s+([\s\S]+?)\s*\%\]": lambda match: convert_mdpath_to_html(os.path.join(base_path, match.group(1))),
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
    for key, value in cfg.items():
        # If the value is a string, preprocess it
        if isinstance(value, str):
            cfg[key] = replace_shortcodes(value)
        # If the value is a dictionary, recursively preprocess it
        elif isinstance(value, dict):
            preprocess_config(value, base_path=base_path)
        # If the value is a list, preprocess each element
        elif isinstance(value, list):
            cfg[key] = [(replace_shortcodes(item) if isinstance(item, str) else preprocess_config(item, base_path=base_path)) for item in value]
    return cfg


# Function to get link target based on input
def get_link_target(input_path):
    # Determine the file extension
    _, extension = os.path.splitext(input_path)

    # For Python files, replace extension with .html
    if extension == ".py":
        return os.path.splitext(input_path)[0] + ".html"

    # For other file types, return the input path unchanged
    return input_path


# Function to convert Markdown string to HTML
def convert_md_to_html(markdown_content):
    return markdown.markdown(textwrap.dedent(markdown_content))


# Function to convert Markdown file to HTML
def convert_mdpath_to_html(markdown_path):
    with open(markdown_path, "r") as f:
        markdown_content = f.read()
        return convert_md_to_html(markdown_content)
