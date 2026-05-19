class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        low = float('inf')
        for price in prices:
            if price < low:
                low = price
            else:
                profit = price - low
                maxp = max(maxp, profit)
        return maxp