import unittest

class pedroEqual(unittest.TestCase):
    def test_name_equal_pedro(self):
        name = "MARIA"
        self.assertEqual(name, "PEDRO")

if __name__ == '__main__':
    unittest.main()