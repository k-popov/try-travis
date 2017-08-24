import unittest
import main

class TestNewPlus(unittest.TestCase):

    def test_two_and_two(self):
        self.assertEqual(main.new_plus(2, 2), 4)

    def test_one_and_one(self):
        self.assertNotEqual(main.new_plus(1, 1), 3)
        self.assertEqual(main.new_plus(1, 1), 2)

if __name__ == '__main__':
    unittest.main()
