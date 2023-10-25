class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0 for num in nums]
        result[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            result[i] = nums[i] * result[i+1]
        
        left_range = nums[0]
        result[0] = result[1]
        for i in range(1, len(nums)):
            if i + 1 < len(nums):
                result[i] = left_range * result[i + 1]
            else:
                result[i] = left_range
            left_range = left_range * nums[i]

        return result
    
"""
 [1, 2, 3, 4]
 l_r = 6
 result: [1, 12, 8, 6]
 """

