import unittest

from main import to_upper, say_hello

class TestSayHello(unittest.TestCase):
    def test_to_upper(self):
        self.assertEqual(to_upper("hello"), "HELLO")
        self.assertEqual(to_upper("world"), "WORLD")

    def test_say_hello(self):
        self.assertEqual(say_hello("Alice"), "Hello, ALICE!")
        self.assertEqual(say_hello("Bob"), "Hello, BOB!")

if __name__ == "__main__":
    unittest.main()  # Run the tests
    