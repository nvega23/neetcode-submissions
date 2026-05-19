class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        m = 0

        for num in prices:
            if num < buy:
                buy = num
            elif num - buy > m:
                m = num - buy
        return m

