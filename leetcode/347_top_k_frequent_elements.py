import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = {}
        for num in nums:
            if num not in num_to_count:
                num_to_count[num] = 0
            num_to_count[num] -=1

        heap = list([(count, num) for num, count in num_to_count.items()])
        heapq.heapify(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


"""
Notes:

Can we assume k << n?

Solution:

1. Naive

Create map num to count
iterate over the map k times to get the top one.
O(k*n)

2. SortedMap integer to count

Iterate through this list, keep the counts of each in a sorted map.
Iterate over top k of sorted map and return.

Space: O(N)
Time: O(Nlog(N))? Yes, due to uniqueness

3: Priority Queue? In memory

    Steps:
    1. Create a map of integer to counts
    2. Iterate over input: update map of integer to counts O(n)
    3. Create array out of the map of (count, value) tuples O(n)
    4. Heapify in place O(n)
    5. Pop k times (Log(n) * k).

    time: O(n) soln, which is optimal because reading input
    space: O(n)


    [1, 1, 1, 2, 2, 3]

    num_to_count:
        1: 3
        2: 2
        3: 1
4. Priroity queue improved (used ChatGPT llm to help)
Steps:
    1. Create a map of integer to counts
    2. Iterate over input: update map of integer to counts O(n)
    3. Create a heap, will keep it size k. O(1)
    4. go through num_to_counts. If heap is "Full", then elminiate lowest value item, add new one in. O(nlogk)

    time: O(n) soln, which is optimal because reading input
    space: O(n). Uses less memort than 3, since we do not need to flatten to array


Run:
    Returned still tuples, did not validate return type


"""

