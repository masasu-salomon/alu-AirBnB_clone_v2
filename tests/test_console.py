import unittest
import os
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel

class TestHBNBCommand(unittest.TestCase):
    """Unit tests for HBNBCommand console"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "File storage test only")
    def test_create_base_model_file_storage(self):
        """Test create command with BaseModel in file storage"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) > 0)  # Check for valid ID
            key = f"BaseModel.{output}"
            self.assertIn(key, storage.all())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "MySQL storage test only")
    def test_create_base_model_db_storage(self):
        """Test create command with BaseModel in DB storage"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) > 0)  # Check for valid ID
            key = f"BaseModel.{output}"
            self.assertIn(key, storage.all())

    def test_quit_command(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()):
            self.assertTrue(self.console.onecmd('quit'))

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.emptyline()
            self.assertEqual(fake_out.getvalue().strip(), "")

if __name__ == '__main__':
    unittest.main()
