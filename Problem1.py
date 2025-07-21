"""
I used a greedy approach where I check if the current day's price is higher than the previous day's. If it is, I add the difference to my total profit since I can buy the previous day and sell today. This way, I capture all the upward trends to maximize profit with multiple transactions.
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit