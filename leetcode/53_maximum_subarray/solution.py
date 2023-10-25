class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    def soln_1(self, nums):
        opt_memo = [0 for i in nums]
        opt_including_i_memo = [0 for i in nums]
        opt_memo[0] = nums[0]
        opt_including_i_memo[0] = nums[0]
        for i in range(1, len(nums)):
            opt_including_i_memo[i] = max(nums[i], opt_including_i_memo[i-1] + nums[i])
            opt_memo[i] = max(opt_memo[i-1], opt_including_i_memo[i])

        return opt_memo[len(nums)-1]



    def soln2(self, nums):
        altitudes = [0 for i in nums]
        altitudes[0] = nums[0]
        has_positive = nums[0] > 0
        maximum = nums[0]
        for i in range(1, len(nums)):
            if not has_positive:
                has_positive = nums[i] > 0
            altitudes[i] = altitudes[i-1] + nums[i]
            maximum = min(nums[0], maximum)

        if has_positive:
            peak = altitudes[0]
            index = 0
            for i, num in enumerate(altitudes):
                if num > peak:
                    peak = num
                    index = i
            result = nums[index]
            running_sum = result
            for i in range(index-1, -1, -1):
                running_sum = running_sum + nums[i]
                result = max(running_sum, result)
            return result
        else:
            return maximum


"""
soln1 notes:
Fresh start.
Can we use inductive approach, as we travel accross?
- Answer/keep answer to a different question as well

At index i, the max subarray is either:
    1. Base Case: i = 0
        - Opt(0) = nums[0]
        - max_subarray including 0 = nums[0]
    2. Inductive step: i > 0
        Opt(i) = Max(Opt(i-1),  max subarray including nums[i])
        max subarray including nums[i] = Max(num[i] + max_subarray including num[i-1], nums[i])

    return Opt(n)

[-2,1,-3,4,-1,2,1,-5,4]
[-2,1,1,4,4,4,5,6,6,6] opt memo
[-2,1,-2,4,3,3,5,6,1,4] max_subarray_including_i memo


soln2 notes:(original)
Notes:

    1. Brute force: check al subarrays.
        (N^2) subarrays.
        can do rolling sum for O(N)

    2. Path to O(N)?

[-2,1,-3,4,-1,2,1,-5,4]
[-2,-1,-4,0,-1,1,2,-3,1]
peak = 2
index = 6
result = 6
running_sum = 6

[1]
[1]
peak = 1
index = 0
result = 1
running_sum = 1

[-1,0,-2,2]
[-1,-1,-3,-1]
[-1,-1,-3,-1]
candidate: -1
curr: -1
Auxillary structures

Is there a structure(s) we can create to compute each subarray sum (i, j) in constant time?
- Even so, there are N^2 subarrays. Does not help.

Need some "stay ahead" algorithm, or running best candidate.

Overlapping subarrays/intervals...
Only need to output the largest sum, which is guaranteed to exist, not the interval.
- Compute while making a pass?

At the beginning, nums[0] is the candidate

Memo:
    1. Sum up to that point
    2. Sum and index of the candidate
    3. Sum from candidate index


Walking algorithm

candidate starts at nums[0]
decision point comes at negative number(down slope)
count sums of up slopes.
Always track current altitutde. Max altitutde of the walk.
Max upward stretch

Doesn't make sense for peak ties...

Break the induction.

Wrong anser first time...
wrong assumption. You may never go uphill...

Assumptions thwat were wrong:
    - Didn't conisder uniqueness of peaks
    - Didn't consider all negative cases
    - Didn't utilize math or scope of inputs/cases wells

How to know when idea is a dead end?
"""
