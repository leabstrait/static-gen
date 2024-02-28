import os
import shutil
from markdown import markdown
from jinja2 import Environment, FileSystemLoader
import yaml


# Load configuration from config.yaml
def load_config():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config


# Function to traverse YAML content and convert Markdown blocks to HTML
def traverse_yaml(yaml_content, base_path=""):
    if isinstance(yaml_content, dict):
        for key, value in yaml_content.items():
            if isinstance(value, str):
                # Check if the value is Markdown content
                if value.strip().startswith("```markdown"):
                    # Extract Markdown content between triple backticks
                    start_index = value.find("```markdown") + len("```markdown")
                    end_index = value.rfind("```")
                    markdown_content = value[start_index:end_index].strip()
                    # Convert Markdown content to HTML
                    html_content = markdown(markdown_content)
                    # Replace Markdown content with HTML
                    yaml_content[key] = html_content
                # Check if the value is a path to a Markdown file
                elif value.endswith(".md"):
                    md_path = os.path.join(base_path, value)
                    with open(md_path, "r") as f:
                        markdown_content = f.read()
                        html_content = markdown(markdown_content)
                        yaml_content[key] = html_content
            elif isinstance(value, dict):
                traverse_yaml(value, base_path=base_path)
            elif isinstance(value, list):
                # Traverse nested lists recursively
                for item in value:
                    traverse_yaml(item, base_path=base_path)
    elif isinstance(yaml_content, list):
        # Traverse lists recursively
        for item in yaml_content:
            traverse_yaml(item, base_path=base_path)
    return yaml_content


# Function to copy assets while preserving directory structure
def copy_assets(source_dir, destination_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".md"):
                # Skip YAML and Markdown files from copying as it is to output directory
                continue
            source_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_path, source_dir)
            destination_path = os.path.join(destination_dir, relative_path)
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            shutil.copyfile(source_path, destination_path)


# Define content and template root directories
config = load_config()

content_dir = config["directories"]["content"]
template_dir = config["directories"]["template"]
script_dir = config["directories"]["script"]
style_dir = config["directories"]["style"]
media_dir = config["directories"]["media"]
output_dir = config["directories"]["output"]
default_template = config["default_template"]

# Load templates
env = Environment(loader=FileSystemLoader(template_dir))


# Process each content file
def process_content(d):
    for root, _, files in os.walk(d):
        for filename in files:
            if not filename.endswith(".yaml"):
                continue

            content_path = os.path.join(root, filename)
            with open(content_path, "r") as f:
                yaml_content = yaml.safe_load(f)
                processed_yaml_content = traverse_yaml(
                    yaml_content.copy(), base_path=root
                )
                template_name = processed_yaml_content.pop(
                    "template", default_template
                )

            # Load template
            template = env.get_template(template_name)

            # Render HTML content passing in config and processed_yaml_content
            config.update(processed_yaml_content)
            rendered_content = template.render(**config)

            # Compute relative path of content file within content directory
            rel_path = os.path.relpath(content_path, content_dir)
            # Construct output path
            output_path = os.path.join(
                output_dir, rel_path.replace(".yaml", ".html")
            )

            # Ensure directory structure exists in the output directory
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            # Write rendered content to output file
            with open(output_path, "w") as f:
                f.write(rendered_content)


process_content(content_dir)

# Copy assets to build directory
copy_assets(content_dir, output_dir)
copy_assets(script_dir, os.path.join(output_dir, "scripts"))
copy_assets(style_dir, os.path.join(output_dir, "styles"))
copy_assets(media_dir, os.path.join(output_dir, "media"))

print(f"Static site generated successfully! Output in {output_dir}")
