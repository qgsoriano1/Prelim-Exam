import unittest

def is_pedro(name):
    return name == "PEDRO"

class TestIsPedro(unittest.TestCase):
    
    def test_name_equal_pedro(self):
        self.assertTrue(is_pedro("PEDRO"))

    def test_name_not_equal_pedro(self):
        self.assertFalse(is_pedro("Maria"))
        self.assertFalse(is_pedro("John"))
        self.assertFalse(is_pedro(""))

if __name__ == '__main__':
    unittest.main()
