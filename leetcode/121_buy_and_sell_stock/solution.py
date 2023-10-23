class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        all_time_low = prices[0]
        for i in range(1, len(prices)):
            all_time_low = min(all_time_low, prices[i])
            max_prof_sell_at_i = prices[i] - all_time_low[i]
            result = max(result, max_prof_sell_at_i)
        return result


"""
[7,1,5,3,6,4]
[7,1,1,1,1,1]
profit = 5

"""
