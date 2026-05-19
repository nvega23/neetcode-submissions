class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy pattern 
        # keep track of the maxProfit and the lowest price seen
        # iterate once, and return the number that will get you the max profit
        lowPart = float('inf')
        maxP = 0

        for price in prices:
            if price < lowPart:
                lowPart = price
            else:
                profit = price - lowPart
                maxP = max(maxP, profit)
        return maxP