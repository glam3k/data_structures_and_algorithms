from abc import ABC, abstractmethod
from typing import Any, Tuple

class PriorityQueue(ABC):
    @abstractmethod
    def add(self, key: Any, value: Any) -> None:
        """
        Add an item with the given key and value to the priority queue.
        
        Args:
            key: The priority key for the item.
            value: The value associated with the key.
        """
        pass

    @abstractmethod
    def min(self) -> Tuple[Any, Any]:
        """
        Return the (key, value) tuple with the minimum key, without removing it.
        
        Returns:
            A tuple containing the (key, value) pair with the minimum key.
        
        Raises:
            ValueError: If the priority queue is empty.
        """
        pass

    @abstractmethod
    def remove_min(self) -> Tuple[Any, Any]:
        """
        Remove and return the (key, value) tuple with the minimum key.
        
        Returns:
            A tuple containing the (key, value) pair with the minimum key.
        
        Raises:
            ValueError: If the priority queue is empty.
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Check if the priority queue is empty.
        
        Returns:
            True if the priority queue is empty, False otherwise.
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """
        Return the number of items in the priority queue.
        
        Returns:
            The number of items in the priority queue.
        """
        pass
