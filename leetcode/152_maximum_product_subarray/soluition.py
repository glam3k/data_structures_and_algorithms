class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        opt = [0] * n
        max_including_i_memo = [0] * n
        min_including_i_memo = [0] * n

        opt[0] = nums[0]
        max_including_i_memo[0] = nums[0]
        min_including_i_memo[0] = nums[0]

        for i in range(1, n):
            opt[i] = max(
                    nums[i],
                    opt[i-1],
                    max_including_i_memo[i-1] * nums[i],
                    min_including_i_memo[i-1] * nums[i],
                    )
                    
            max_including_i_memo[i] =  max(
                        nums[i],
                        max_including_i_memo[i-1] * nums[i],
                        min_including_i_memo[i-1] * nums[i],
                        )
            min_including_i_memo[i] =  min(
                        nums[i],
                        max_including_i_memo[i-1] * nums[i],
                        min_including_i_memo[i-1] * nums[i],
                        )
        return opt[n-1]



if __name__ == '__main__':
    soln = Solution()
    example_1 = [2, 3, -2, 4]
    example_2 = [-2, 0, -1]
    example_3 = [-2, 0, 1]
    print(soln.maxProduct(example_1))
    print(soln.maxProduct(example_2))
    print(soln.maxProduct(example_3))

"""
Notes:

n is >=1

Recursive
max_product_subarray_including_i
min_product_subarray_including_i

1. Base Case (n = 1)
    opt(1) = nums[0]
    max_product_subarray_including_i[1] = nums[0]
    min_product_subarray_including_i[1] = nums[0]
2. Recursive Case (n > 1)
    opt(n) = max(opt(n-1), max_product_subarray_including_i[n-1] * nums[n], min_product_subarray_including_i[n-1] * nums[n], nums[n])j
    max_product_subarray_including_i[n] =  min(nums[n], min_product_subarray_including_i[n-1] * n, max_product_subarray_including_i[n-1])
    min_product_subarray_including_i[n] =  max(nums[n], min_product_subarray_including_i[n-1] * nums[n], max_product_subbarray_including_i[n-1])

Examples
example_1:
[2, 3, -2, 4]

opt - [2, 6, 6, 6]
max_memo - [2, 6, -2, 4]
min_memo - [2, 3, -12, -48]
return 6


example_2
[-2, 0, -1]
opt = [-2, 0, 0]
max_memo = [-2, 0, 0]
min_memo = [-2, 0, -1]
return 0

example_3:
[i]

trivially returns i

example_4:
[-4, -2, 3, 4]

Review:
Correct. Try to use constant space for thes sorts of things.

"""
