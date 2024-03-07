import pytest
import shutil
import os
from staticgen.cli import init_project, main


@pytest.fixture(scope="module")
def temp_dir():
    # Create a temporary directory for testing
    temp_dir = "temp_test_dir"
    os.makedirs(temp_dir, exist_ok=True)
    yield temp_dir
    # Teardown: remove the temporary directory after the test
    shutil.rmtree(temp_dir)


def test_gen(temp_dir):
    # Initialize the project in the temporary directory
    init_project(temp_dir)

    # Call the main function to generate the static site
    os.chdir(temp_dir)
    main(["gen"])

    # Check if the 'docs' directory exists
    assert os.path.exists("docs")

    # Check if the 'docs' directory contains the expected files
    assert os.path.exists(os.path.join("docs", "index.html"))
    os.chdir("..")
