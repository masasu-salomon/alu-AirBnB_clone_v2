import unittest
import MySQLdb
import os
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models import storage
from models.place import Place

class TestMySQLPlace(unittest.TestCase):
    """Unit tests for MySQL storage with Place model"""

    def setUp(self):
        """Set up MySQL connection and environment"""
        self.db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST', 'localhost'),
            user=os.getenv('HBNB_MYSQL_USER', 'hbnb_test'),
            passwd=os.getenv('HBNB_MYSQL_PWD', 'hbnb_test_pwd'),
            db=os.getenv('HBNB_MYSQL_DB', 'hbnb_test_db')
        )
        self.cursor = self.db.cursor()
        os.environ['HBNB_TYPE_STORAGE'] = 'db'

    def tearDown(self):
        """Close MySQL connection"""
        self.db.close()

    def get_place_count(self):
        """Helper method to get current number of places in database"""
        self.cursor.execute("SELECT COUNT(*) FROM places")
        return self.cursor.fetchone()[0]

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "MySQL storage not active")
    def test_create_place(self):
        """Test that creating a Place via console adds a record to places table"""
        initial_count = self.get_place_count()
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            console = HBNBCommand()
            console.onecmd('create Place city_id="CA123" user_id="USER123" name="Cozy_Cabin" number_rooms=2')
        
        final_count = self.get_place_count()
        self.assertEqual(final_count, initial_count + 1)
        
        self.cursor.execute("SELECT name, city_id, number_rooms FROM places ORDER BY created_at DESC LIMIT 1")
        place_data = self.cursor.fetchone()
        self.assertEqual(place_data[0], "Cozy_Cabin")
        self.assertEqual(place_data[1], "CA123")
        self.assertEqual(place_data[2], 2)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "MySQL storage not active")
    def test_create_place_invalid_city_id(self):
        """Test that creating a Place with invalid city_id does not add a record"""
        initial_count = self.get_place_count()
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            console = HBNBCommand()
            console.onecmd('create Place city_id="INVALID" user_id="USER123" name="Invalid_Place"')
        
        final_count = self.get_place_count()
        self.assertEqual(final_count, initial_count)  # No record should be added

if __name__ == '__main__':
    unittest.main()
