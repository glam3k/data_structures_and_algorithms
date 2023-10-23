class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i, num in enumerate(nums):
            if target - nums in m:
               return [m[target - nums], i] 
            m[num] = i
        return None

