import unittest
from xguard import guard

class TestXguard(unittest.TestCase):

    def setUp(self):
        self.guard = guard.Xguard()

    def test_not_null(self):
        with self.assertRaises(ValueError):
            self.guard.not_null(None)
        self.assertEqual(self.guard.not_null('hello'), self.guard)

    def test_is_type(self):
        with self.assertRaises(TypeError):
            self.guard.is_type('hello', int)
        self.assertEqual(self.guard.is_type(123, int), self.guard)

    def test_is_gt(self):
        with self.assertRaises(TypeError):
            self.guard.is_gt(5, 10)
        self.assertEqual(self.guard.is_gt(10, 5), self.guard)

if __name__ == '__main__':
    unittest.main()
