class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        for price in range(1,len(prices)):
            if prices[price] < min:
                min = prices[price]
            if prices[price] - min > profit:
                profit = prices[price] - min 

        return profit