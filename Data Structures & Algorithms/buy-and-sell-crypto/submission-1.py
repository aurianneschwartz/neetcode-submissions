class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_seen = prices[0]
        profit = 0
        
        for price in range(1,len(prices)):      
            min_seen = min(min_seen, prices[price])
            profit = max(prices[price] - min_seen, profit)

        return profit