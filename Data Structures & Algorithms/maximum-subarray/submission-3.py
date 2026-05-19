class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxn = nums[0]
        low = 0

        for num in nums:
            low = max(low, 0)
            low += num
            maxn = max(maxn, low)
        return maxn