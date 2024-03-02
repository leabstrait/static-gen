# Verifies the copying of assets to the output directory.

import os
import shutil
import tempfile
import unittest


class TestCopyAssets(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_copy_assets(self):
        from staticgen import copy_assets
        copy_assets()