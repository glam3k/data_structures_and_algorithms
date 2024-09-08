import unittest
from typing import Any, Tuple
from heap_priority_queue import HeapPriorityQueue

class TestHeapPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = HeapPriorityQueue()

    def test_empty_queue(self):
        self.assertTrue(self.pq.is_empty())
        self.assertEqual(len(self.pq), 0)
        with self.assertRaises(ValueError):
            self.pq.min()
        with self.assertRaises(ValueError):
            self.pq.remove_min()

    def test_single_element(self):
        self.pq.add(5, "five")
        self.assertFalse(self.pq.is_empty())
        self.assertEqual(len(self.pq), 1)
        self.assertEqual(self.pq.min(), (5, "five"))
        self.assertEqual(self.pq.remove_min(), (5, "five"))
        self.assertTrue(self.pq.is_empty())

    def test_multiple_elements(self):
        elements = [(3, "three"), (1, "one"), (4, "four"), (1, "uno"), (5, "five"), (2, "two")]
        for k, v in elements:
            self.pq.add(k, v)
        
        self.assertEqual(len(self.pq), 6)
        self.assertEqual(self.pq.min(), (1, "one"))  # Assuming it returns the first added in case of tie
        
        # Test removing all elements
        sorted_elements = sorted(elements, key=lambda x: (x[0], elements.index(x)))
        for expected in sorted_elements:
            self.assertEqual(self.pq.remove_min(), expected)
        
        self.assertTrue(self.pq.is_empty())

    def test_add_and_remove(self):
        self.pq.add(3, "three")
        self.pq.add(1, "one")
        self.pq.add(2, "two")
        
        self.assertEqual(self.pq.remove_min(), (1, "one"))
        self.assertEqual(len(self.pq), 2)
        
        self.pq.add(0, "zero")
        self.assertEqual(self.pq.min(), (0, "zero"))
        self.assertEqual(len(self.pq), 3)
        self.assertEqual(self.pq.remove_min(), "zero")

    def test_min_without_remove(self):
        self.pq.add(3, "three")
        self.pq.add(1, "one")
        self.assertEqual(self.pq.min(), (1, "one"))
        self.assertEqual(len(self.pq), 2)  # Ensure min() doesn't remove the element
        self.assertEqual(self.pq.min(), (1, "one"))  # Can call min() multiple times

    def test_add_duplicate_keys(self):
        self.pq.add(1, "one")
        self.pq.add(1, "uno")
        self.assertEqual(len(self.pq), 2)
        self.assertEqual(self.pq.remove_min(), (1, "one"))  # Assuming FIFO for same keys
        self.assertEqual(self.pq.remove_min(), (1, "uno"))

    def test_add_negative_keys(self):
        self.pq.add(-1, "minus one")
        self.pq.add(1, "one")
        self.assertEqual(self.pq.remove_min(), (-1, "minus one"))

    def test_large_number_of_elements(self):
        for i in range(1000):
            self.pq.add(1000 - i, f"item{i}")
        
        self.assertEqual(len(self.pq), 1000)
        self.assertEqual(self.pq.min(), (1, "item999"))

        for i in range(1000):
            expected = (i + 1, f"item{999-i}")
            self.assertEqual(self.pq.remove_min(), expected)

    def test_key_types(self):
        # Test with different comparable types
        self.pq.add(3.14, "pi")
        self.pq.add("apple", "fruit")
        self.pq.add((1, 2), "tuple")
        
        self.assertEqual(self.pq.remove_min(), ((1, 2), "tuple"))
        self.assertEqual(self.pq.remove_min(), (3.14, "pi"))
        self.assertEqual(self.pq.remove_min(), ("apple", "fruit"))

if __name__ == '__main__':
    unittest.main()
