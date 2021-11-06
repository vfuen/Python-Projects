import unittest
from full_name import full_names

class VerifyNames(unittest.TestCase):
    """Test if names work for full_name.py"""
    def test_first_last(self):
        full = full_names(
            'tim', 'harris')
        self.assertEqual(full, 'Tim Harris')

    def test_first_middle_last(self):
        """Test middle name"""
        full_with_middle = full_names(
            'tim', 'harris', 'pinnleton')
        self.assertEqual(full_with_middle, 'Tim Pinnleton Harris')

    if __name__ == '__main__':
        unittest.main()

