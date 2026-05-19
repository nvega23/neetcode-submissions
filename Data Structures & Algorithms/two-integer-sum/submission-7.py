class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in output:
                return [output[diff], i]
            output[nums[i]] = i
