from priority_queue import PriorityQueue
from typing import Any, Tuple

INITIAL_SIZE = 12
RESIZE_FACTOR = 2

class HeapPriorityQueue(PriorityQueue):
    """
    Uses array representation of tree

    """

    def __init__(self):
        self._heap = [None] * INITIAL_SIZE
        self._size = 0

    def add(self, key: Any, value: Any) -> None:
        """
        Add an item with the given key and value to the priority queue.
        
        Args:
            key: The priority key for the item.
            value: The value associated with the key.
        """
        if self._size == len(self._heap):
            self._resize(len(self._heap) * RESIZE_FACTOR)

        self._heap[self._size] = (key, value)
        self._bubble_up(self._size)

        self._size = self._size + 1

    def min(self) -> Tuple[Any, Any]:
        """
        Return the (key, value) tuple with the minimum key, without removing it.
        
        Returns:
            A tuple containing the (key, value) pair with the minimum key.
        
        Raises:
            ValueError: If the priority queue is empty.
        """
        if self.is_empty():
            raise ValueError
        return self._heap[0]

    def remove_min(self) -> Tuple[Any, Any]:
        """
        Remove and return the (key, value) tuple with the minimum key.
        
        Returns:
            A tuple containing the (key, value) pair with the minimum key.
        
        Raises:
            ValueError: If the priority queue is empty.
        """
        
        if self.is_empty():
            raise ValueError
        
        result = self._heap[0]
        self._heap[0] = self._heap[self._size - 1]
        self._heap[self._size - 1] = None
        self._size = self._size - 1

        self._bubble_down(0)

        if self._size != 0 and len(self._heap) / self._size >= RESIZE_FACTOR**2:
            self._resize(len(self._heap) // RESIZE_FACTOR)

        return result

    def is_empty(self) -> bool:
        """
        Check if the priority queue is empty.
        
        Returns:
            True if the priority queue is empty, False otherwise.
        """
        return self._size == 0

    def __len__(self) -> int:
        """
        Return the number of items in the priority queue.
        
        Returns:
            The number of items in the priority queue.
        """
        return self._size

    def _bubble_up(self, i):
        while ((i - 1) // 2 >= 0) and self._heap[(i - 1) // 2][0] > self._heap[i][0]:
            self._heap[(i - 1) // 2],  self._heap[i] = self._heap[i], self._heap[(i - 1) // 2]
            i = (i - 1) // 2

    def _bubble_down(self, i):
        # while it has a child with a lesser key, swap position with lesser
        # key child
        while (
                (2*i+1 < self._size and self._heap[2*i+1][0] < self._heap[i][0])
                or (2*i+2 < self._size and self._heap[2*i+2][0] < self._heap[i][0])
                ):
            # has right child with lesser key, and right child has leser key than
            # left child
            if 2*i+2 < self._size and self._heap[2*i+2][0] < self._heap[i][0] and self._heap[2*i+2][0] < self._heap[2*i+1][0]: 
                self._heap[i], self._heap[2*i+2] = self._heap[2*i+2], self._heap[i]
                i = 2*i+2
            else: # swap with left child
                self._heap[i], self._heap[2*i+1] = self._heap[2*i+1], self._heap[i]
                i = 2*i+1

    def _resize(self, new_size: int):
        assert self._size < new_size
        new_heap = [None] * new_size
        for i in range(self._size):
            new_heap[i] = self._heap[i]
        self._heap =  new_heap
