class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxn = nums[0]
        currs = 0

        for num in nums:
            currs = max(currs, 0)
            currs += num
            maxn = max(maxn, currs)
        return maxn