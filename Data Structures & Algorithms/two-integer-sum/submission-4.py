class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate over the array twice
        # check if one index + the next index equals the target
        # return the two indexes in an array
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
