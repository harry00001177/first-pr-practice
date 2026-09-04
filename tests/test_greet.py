import unittest

from greet import greet


class GreetTests(unittest.TestCase):
    def test_greets_by_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_falls_back_when_name_is_empty(self):
        self.assertEqual(greet(""), "Hello, stranger!")

    def test_falls_back_when_name_is_none(self):
        self.assertEqual(greet(None), "Hello, stranger!")


if __name__ == "__main__":
    unittest.main()
