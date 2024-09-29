import heapq
class MedianFinder:

    def __init__(self):
        # Will hold -1*num to make a Max heap.
        # Must remember to convert numbers before pushing and after popping.
        self._lessThanHalf = [] 
        self._greaterThanHalf = []
      
    @staticmethod
    def _negate(num: int) -> int:
        return -1*num

    def addNum(self, num: int) -> None:
        # first addNum case
        if not self._lessThanHalf: 
            heapq.heappush(self._lessThanHalf, MedianFinder._negate(num))
        elif not self._greaterThanHalf: # second addNum case
            if num < MedianFinder._negate(self._lessThanHalf[0]):
                greaterNum = MedianFinder._negate(heapq.heappop(self._lessThanHalf))
                heapq.heappush(self._lessThanHalf, MedianFinder._negate(num))
                heapq.heappush(self._greaterThanHalf, greaterNum)
            else:
                heapq.heappush(self._greaterThanHalf, num)
        else: # General case.
            if num <= MedianFinder._negate(self._lessThanHalf[0]):
                heapq.heappush(self._lessThanHalf, MedianFinder._negate(num))
            else:
                heapq.heappush(self._greaterThanHalf, num)
            
            if len(self._lessThanHalf) - len(self._greaterThanHalf) == 2:
                numToMove = MedianFinder._negate(heapq.heappop(self._lessThanHalf))
                heapq.heappush(self._greaterThanHalf, numToMove)
            elif len(self._lessThanHalf) - len(self._greaterThanHalf) == -1:
                numToMove = heapq.heappop(self._greaterThanHalf)
                heapq.heappush(self._lessThanHalf, MedianFinder._negate(numToMove))



    def findMedian(self) -> float:
        if len(self._lessThanHalf) == len(self._greaterThanHalf):
            return (MedianFinder._negate(self._lessThanHalf[0]) + self._greaterThanHalf[0]) / 2
        else:
            return (MedianFinder._negate(self._lessThanHalf[0]))

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
Notes
- even list, no median
- type is float, just needs to be within close bound

Key idea: you don't care about all behind the middle two, you just need the middle two
j
Solution:
1. Naive

Keep list/store of all numbers. Sort and compute median each query to findMedian
addNum: O(1)
findMedian(O(NlogN)  (sort whole list and go to middle value)
space: O(n)

2. Sorted List

Keep SortedList of all numbers.

addNum: O(nlogn): insert a number into a list and keep in sorted order
findMedian: O(1): jump right to middle
space: O(n)

3. Search Tree / SortedSet

4. 2 priority queues
Key idea: When finding the median, we just need to hone in on the "middle".
No walk or arithmetic needs to be done on the whole set of numbers.

We must bias towards one.
Bias toward lessThanHalf

lessThanHalf PriorityQueue
- Max queue

greaterThanHalf Priority queue
- min queue

Invariants
0 <= len(lessThanHalf) - len(greaterThanHalf) <= 1

addNum:
    1. Check which half it belongs in O(1)
    2. Add to that half O(logn)
    3. Fix to maintain invariant(remove from larger side) O(logn)

findMedian:
    1. If both halfs are same size,
        there is no median. Return None
    2. Else:
        be the top of the lessThanHalf
    

Testing:
    1. check all lessThanHalf do the negation on insert/pop
    2. Ensure invariant that less half is always 0 or 1 more than greaterHalf
Scratchpad:

"""
