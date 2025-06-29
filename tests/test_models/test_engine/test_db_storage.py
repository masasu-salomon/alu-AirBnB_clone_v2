import unittest
from models.engine.db_storage import DBStorage

class TestDBStorage(unittest.TestCase):
    """Basic tests for DBStorage class"""

    def setUp(self):
        self.storage = DBStorage()

    def test_instance(self):
        """Test DBStorage instance creation"""
        self.assertIsInstance(self.storage, DBStorage)

    # Add more tests as needed for your project

if __name__ == "__main__":
    unittest.main()
