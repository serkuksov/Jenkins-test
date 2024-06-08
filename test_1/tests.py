import unittest
from unittest import TestCase

from main import add


class Test(TestCase):
    def test(self):
        self.assertEqual(add(1, 2), 3, "Сложение")


if __name__ == '__main__':
    unittest.main()
