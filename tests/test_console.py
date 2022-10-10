#!/usr/bin/python3
"""Console Unittest"""

import unittest
from io import StringIO
from unittest.mock import patch
import pep8
import os
from os import getenv
import console
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """The console test class"""

    @classmethod
    def setUpClass(cls):
        """Class setup for testing"""
        cls.console = HBNBCommand()

    def setUp(self):
        """Setting up test cases"""
        if os.path.isfile('file.json'):
            os.remove('file.json')
        self.resetStorage()

    def resetStorage(self):
        """Resetting the file storage"""
        FileStorage._FileStorage__objects = {}

        if os.path.isfile(FileStorage._FileStorage__objects):
            os.remove(FileStorage._FileStorage__objects)

    def test_pep8_console(self):
        """Pep8 test for console"""
        style = pep8.StyleGuide(quiet=True)
        checker = style.check_files(["console.py"])
        self.assertEqual(checker.total_errors, 0, 'fix Pep8')

    def test_docstrings_in_console(self):
        pass

    def test_create(self):
        pass

    def test_quit(self):
        pass

    def test_emptyline(self):
        pass
