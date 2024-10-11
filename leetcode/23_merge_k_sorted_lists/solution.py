# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # entries of form (val: int, id: int, node: ListNode)
        heap = [] # could predeclare size here, but dont want to due to possibly empty lists

        for list_id, node in enumerate(lists):
            if node is not None:
                heap.append((node.val, list_id, node))
        if not heap:
            return None
        
        heapq.heapify(heap)
        _, list_id, result =  heapq.heappop(heap)
        if result.next is not None:
            heapq.heappush(heap, (result.next.val, list_id, result.next))
        curr = result
    
        while heap:
            _, list_id, smallest = heapq.heappop(heap)
            if smallest.next is not None:
                heapq.heappush(heap, (smallest.next.val, list_id, smallest.next))
            curr.next = smallest
            curr = curr.next
        
        curr.next = None
        return result 
                
        

"""
Notes:

suppose each list is n.
Best case is only read through each list once, so O(k*n)

Q: Are all list nonempty, or not none? (size >= 1)?
A: Some lists can be empty

Q: Do we need to make copies, or can we actually mutate the input?

Q: Should we ever return None?
- No. can return [] on edge cases

Solutions:

1. Naive solution:
    Steps:
        1. Initialize empty result 
        2. Keep track of nonempty lists
        3. Iterate through all nonempty list, find smallest.
        4. Add add smallest to result, and remove from nomempty list
        5. If candidate list becomes empty, remove from pool(micro optimization, does not change overall complexity)
        6. When all lists are empty return result

    time: O(k^2*n)
    space: O(n) no new space created if mutation allowed

2: Priority Queue for next candidate.
        1. Initialize empty result  O(1)
        2. Keep track of nonempty lists 
        3. initalize priority queue we limit to size k O(k) sharp or O(klogk) 
        4. while priority queue is nonempty,
            - Pop the smallest, add to result
            - get next item in list that was popped, add to priority queue
        
        Eventually, all items will end up in the priority queue

Each iteration is a pop and insertion so 2* O(logk)
k*n iterations
time: O(logk*nk)
space: O(k) auxillary for priority queue

3. ???
"""
