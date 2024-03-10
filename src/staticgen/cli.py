import argparse
import shutil
import os
import importlib.resources
from staticgen import staticgen


def init_project(destination):
    # If destination is not provided or is '.', use the current directory
    if destination is None or destination == ".":
        destination = os.getcwd()

    # Check if the specified directory already exists
    if os.path.exists(destination):
        if os.listdir(destination):
            print(f"Error: Directory '{destination}' already exists and is not empty.")
            if not input("Do you still want to proceed? [y/N]: ").lower() == "y":
                return

    starter_project_dir = importlib.resources.files("staticgen").joinpath("starter_project")

    try:
        os.makedirs(destination, exist_ok=True)
        # Copy starter project files to the destination directory
        shutil.copytree(
            str(starter_project_dir),
            destination,
            dirs_exist_ok=True,
        )
        print(f"Starter project initialized in: {destination}")
    except Exception as e:
        print(f"Error initializing starter project: {e}")


def main(args=None):
    """
    Main entry point for the CLI.
    """
    parser = argparse.ArgumentParser(description="Static Site Generator CLI")
    parser.add_argument("command", choices=["init", "gen"], help="Command to execute")
    parser.add_argument("--destination", help="Destination directory for init command")

    if args is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    if args.command == "init":
        init_project(args.destination)
    elif args.command == "gen":
        staticgen.main()
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
