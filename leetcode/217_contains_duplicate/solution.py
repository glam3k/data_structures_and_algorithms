class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       m = set()
       for num in nums:
           if num in m:
               return True
            m.add(num)
        return False
    
