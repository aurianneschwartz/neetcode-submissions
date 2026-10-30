class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minimum = [float('inf')] * (amount + 1)
        minimum[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    minimum[i] = min(minimum[i], minimum[i - coin] + 1)

        if minimum[amount] == float('inf'):
            return -1
        return minimum[amount]