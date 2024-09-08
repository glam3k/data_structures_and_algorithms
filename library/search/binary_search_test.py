import unittest
from typing import Any, Sequence, Optional

# Assuming your function is in a file named 'search_algorithms.py'
from binary_search import binary_search_iterative, binary_search_recursive

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_iterative(self):
        self._test_binary_search(binary_search_iterative)

    def test_binary_search_recursive(self):
        self._test_binary_search(binary_search_recursive)

    def _test_binary_search(self, fn):
        test_cases = [
            (3, [1, 2, 3, 4, 5], 2),
            (1, [1, 2, 3, 4, 5], 0),
            (5, [1, 2, 3, 4, 5], 4),
            (6, [1, 2, 3, 4, 5], None),
            (0, [1, 2, 3, 4, 5], None),
            (3, [3], 0),
            (1, [2], None),
            (1, [], None),
            ("apple", ["apple", "banana", "cherry", "date"], 0),
            ("date", ["apple", "banana", "cherry", "date"], 3),
            ("grape", ["apple", "banana", "cherry", "date"], None),
        ]

        for item, items, expected in test_cases:
            with self.subTest(item=item, items=items):
                result = fn(item, items)
                self.assertEqual(result, expected)

    def test_large_input(self):
        large_list = list(range(1000000))
        self.assertEqual(binary_search_iterative(500000, large_list), 500000)
        self.assertEqual(binary_search_iterative(-1, large_list), None)
        self.assertEqual(binary_search_iterative(1000000, large_list), None)

if __name__ == '__main__':
    unittest.main()
