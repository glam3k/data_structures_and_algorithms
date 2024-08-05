class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * n
        return self.topDownSolutionHelper(n, memo)

    def topDownSolutionHelper(self, n: int, memo) -> int:
        if memo[n - 1]:
            return memo[n-1]
        if n == 1:
            memo[0] = 1
            return 1
        elif n == 2:
            memo[1] = 2
            return 2
        else:
           memo[n-1] = self.topDownSolutionHelper(n - 1, memo) + self.topDownSolutionHelper(n - 2, memo)
           return memo[n-1]



        
"""
Notes

Recursive/DP problem/algorithm.
- has multiple base cases

Opt(n) is 
1. Base Case (n==0)
    Opt(0) == 0
2. Base Case (n==1) 
    Opt(1) = 1 
3. Base Case (n==2) << NOT NECCESSARY
    Opt(2) == 2
    1. Can go 1, 1 OR 2
4. Suppose n >= 3; Opt(n) == (Opt(n-1)) + (Opt(n-2))

It is fibonnaci!

Manually verify for small cases:
opt(3) = 3
1. 1 1 1
2. 1 2
3. 2 1

AVOID double counting:
Note that taking a single step after Opt(n-2) counts towards one of the solutions
to Opt(n-1). There is only on way to go up one step though.


Let us to top down memo and bottom up.

TODO: Analyze recursive/recurrences top down algorithms.
N cannot be 0.

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        memo = [0 * n]
        memo[0] = 1
        memo[1] = 2
        for i in range(2, n):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n-1]


"""
