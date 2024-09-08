from typing import Optional, Sequence, Any
 
def binary_search_iterative(item: Any, items: Sequence[Any]) -> Optional[int]:
    lo = 0
    hi = len(items) - 1
    while (lo <= hi):
        mid = (lo + hi) // 2
        if items[mid] == item:
            return mid
        elif items[mid] < item:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def binary_search_recursive(item: Any, items: Sequence[Any]):
    def _binary_search_recursive(item: Any, items: Sequence[Any], lo: int, hi: int):
        if lo > hi:
            return None
        else:
            mid = (lo + hi) // 2
            if items[mid] == item:
                return mid
            elif items[mid] < item:
                lo = mid + 1
            else:
                hi = mid - 1
        return _binary_search_recursive(item, items, lo, hi)


    return _binary_search_recursive(item, items, 0, len(items) -1)
