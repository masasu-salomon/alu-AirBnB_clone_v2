#!/usr/bin/python3
""" Unit tests for the console """
import unittest
from console import HBNBCommand
import sys
from io import StringIO
import json
import os


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

    def test_create_with_params(self):
        """Test create command with parameters"""
        self.console.onecmd('create State name="California"')
        state_id = self.output.getvalue().strip().split('\n')[-1]
        self.assertTrue(len(state_id) > 0)
        self.output.truncate(0)
        self.output.seek(0)
        self.console.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
        place_id = self.output.getvalue().strip().split('\n')[-1]
        self.assertTrue(len(place_id) > 0)

    def test_create_string_escape_and_underscore(self):
        """Test string value with escaped quotes and underscores"""
        self.console.onecmd('create State name="My_little_\"house\""')
        state_id = self.output.getvalue().strip().split('\n')[-1]
        self.assertTrue(len(state_id) > 0)

    def test_create_invalid_param(self):
        """Test create skips invalid params"""
        self.console.onecmd('create State name="Valid" badparam')
        state_id = self.output.getvalue().strip().split('\n')[-1]
        self.assertTrue(len(state_id) > 0)

    def test_create_state_id_in_file(self):
        """Test that create State adds the new ID to file.json (FileStorage)"""
        # Remove file.json if it exists to start fresh
        if os.path.exists('file.json'):
            os.remove('file.json')
        self.output.truncate(0)
        self.output.seek(0)
        self.console.onecmd('create State name="TestState"')
        state_id = self.output.getvalue().strip().split('\n')[-1]
        self.assertTrue(len(state_id) > 0)
        # Now check file.json for the new State ID
        with open('file.json', 'r') as f:
            data = json.load(f)
        found = any(state_id in key for key in data.keys())
        self.assertTrue(found, f"State ID {state_id} not found in file.json")


if __name__ == "__main__":
    unittest.main()
