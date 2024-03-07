import pytest
import shutil
import os
from importlib.resources import files as res_files
from staticgen.cli import init_project


@pytest.fixture(scope="module")
def temp_dir():
    # Create a temporary directory for testing
    temp_dir = "temp_test_dir"
    os.makedirs(temp_dir, exist_ok=True)
    yield temp_dir
    # Teardown: remove the temporary directory after the test
    shutil.rmtree(temp_dir)


def check_files(temp_dir, package_files):
    # Recursively iterate through the files and directories in package_files
    # compare them to the files in the temporary directory
    for item in package_files.iterdir():
        temp_item_path = os.path.join(temp_dir, item.name)
        if item.is_file():
            assert os.path.isfile(temp_item_path)
            assert item.read_bytes() == open(temp_item_path, "rb").read()
        elif item.is_dir():
            assert os.path.isdir(temp_item_path)
            check_files(temp_item_path, item)


def test_init(temp_dir):
    # Get the path to the expected files in the package source
    package_files = res_files("staticgen").joinpath("starter_project")

    # Call init_project function with the temporary directory as destination
    init_project(temp_dir)

    # Check if the copied files match the expected files
    check_files(temp_dir, package_files)
