class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        output = {}
        for i in range(len(nums)):
            if nums[i] in output and i - output[nums[i]] <= k:
                return True
            output[nums[i]] = i
        return False
