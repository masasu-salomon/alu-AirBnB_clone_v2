#!/usr/bin/python3
""" Unit tests for the console """
import unittest
from console import HBNBCommand
import sys
from io import StringIO


class TestConsole(unittest.TestCase):
    """Test the console commands"""

    def setUp(self):
        self.console = HBNBCommand()
        self.output = StringIO()
        self._stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = self._stdout

    def test_quit_command(self):
        """Test quit command exits the console"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF_command(self):
        """Test EOF command exits the console"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_emptyline(self):
        """Test empty line does nothing"""
        self.console.onecmd("")
        self.assertEqual(self.output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
