import os
import shutil

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
