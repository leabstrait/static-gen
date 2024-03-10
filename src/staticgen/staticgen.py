import os
from jinja2 import Environment, FileSystemLoader
import importlib.util
from .utils import shortcodes
from .utils import assets

# Function to process each content file
def process_content(jinjaenv, config_p, directory):
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
            processed_content_config = shortcodes.preprocess_config(module.config, base_path=root)

            # Get template name and remove it from processed content config
            template_name = processed_content_config.pop("template", config_p["default_template"])

            # Load template
            template = jinjaenv.get_template(template_name)

            # Render HTML content passing in config and processed_content_config
            rendered_content = template.render(
                **{key: value for key, value in config_p.items() if key not in processed_content_config.keys()},
                **processed_content_config,
            )

            # Compute relative path of content file within content directory
            rel_path = os.path.relpath(content_path, config_p["directories"]["content"])
            # Construct output path
            output_path = os.path.join(config_p["directories"]["output"], rel_path.replace(".py", ".html"))

            # Ensure directory structure exists in the output directory
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            # Write rendered content to output file
            with open(output_path, "w") as f:
                f.write(rendered_content)


def main():
    config_path = os.path.join(".", "config.py")
    spec = importlib.util.spec_from_file_location("config", config_path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    config_p = shortcodes.preprocess_config(config.config, base_path="")

    # Load templates into Jinja environment
    jinjaenv = Environment(loader=FileSystemLoader(config.config["directories"]["template"]))

    # Process content files
    content_dir = config_p["directories"]["content"]
    process_content(jinjaenv, config_p, content_dir)

    # Copy assets to output directory
    assets.copy_assets(
        config_p["directories"]["script"],
        os.path.join(config_p["directories"]["output"], "scripts"),
    )
    assets.copy_assets(
        config_p["directories"]["style"],
        os.path.join(config_p["directories"]["output"], "styles"),
    )
    assets.copy_assets(
        config_p["directories"]["media"],
        os.path.join(config_p["directories"]["output"], "media"),
    )
    assets.copy_assets(
        config_p["directories"]["content"],
        config_p["directories"]["output"],
    )

    print(f"Static site generated successfully! Output in {config_p['directories']['output']}")
