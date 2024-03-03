import argparse
import shutil
import pkg_resources
import os


def init_project(destination):
    # If destination is not provided or is '.', use the current directory
    if destination is None or destination == '.':
        destination = os.getcwd()

    # Check if the specified directory already exists
    if os.path.exists(destination) and os.listdir(destination):
        print(f"Error: Directory '{destination}' already exists and is not empty.")
        return

    os.makedirs(destination)

    # Logic for initializing a starter project
    # Path to the directory containing the starter project files
    starter_project_dir = pkg_resources.resource_filename(
        "staticgen", "starter_project"
    )

    try:
        # Copy starter project files to the destination directory
        shutil.copytree(starter_project_dir, destination, dirs_exist_ok=True)
        print(f"Starter project initialized in: {destination}")
    except Exception as e:
        print(f"Error initializing starter project: {e}")


def main():
    parser = argparse.ArgumentParser(description="Static Site Generator CLI")
    parser.add_argument("command", choices=["init", "gen"], help="Command to execute")
    parser.add_argument(
        "--destination", help="Destination directory for init command"
    )

    args = parser.parse_args()

    if args.command == "init":
        init_project(args.destination)
    elif args.command == "gen":
        from staticgen import staticgen
        staticgen.main()
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
