class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_prices = 0, float('inf')
        
        for p in prices:
            min_prices = min(p, min_prices)
            profit = p-min_prices
            max_profit = max(profit, max_profit)
        return max_profit