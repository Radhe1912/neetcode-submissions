class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_min = prices[0]

        for i in prices:
            profit = max(profit, i-curr_min)
            curr_min = min(curr_min, i)

        return profit