class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_prices = 0, float('inf')  # float('inf') => 양의 무한대
        
        for p in prices:
            min_prices = min(p, min_prices)  # 양의 무한대 값과 prices 값을 비교
            profit = p-min_prices
            max_profit = max(profit, max_profit)
        return max_profit