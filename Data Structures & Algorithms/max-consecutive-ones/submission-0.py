class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maxC = 0
        for num in nums:
            if num == 0:
                maxC = max(maxC, count)
                count = 0
            else:
                count += 1
        return max(maxC, count)