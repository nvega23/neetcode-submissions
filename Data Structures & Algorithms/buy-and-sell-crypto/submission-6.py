class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        maxp = 0
        for price in prices:
            if price < low:
                low = price
            else:
                profit = price - low
                maxp = max(maxp, profit)
        return maxp