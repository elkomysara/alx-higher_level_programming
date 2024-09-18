import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Unit tests for the Base class"""

    def test_id_assignment(self):
        """Test that the id is assigned correctly."""
        b1 = Base()
        b2 = Base(100)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 100)

if __name__ == "__main__":
    unittest.main()
