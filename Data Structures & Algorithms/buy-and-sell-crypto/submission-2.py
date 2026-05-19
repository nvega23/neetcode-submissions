class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        max_p = 0
        for price in prices:
            if price < low:
                low = price
            else:
                profit = price - low
                max_p = max(max_p, profit)
        return max_p
            