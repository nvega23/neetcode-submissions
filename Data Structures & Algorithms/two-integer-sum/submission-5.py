class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate over array
        # iterate over array with the index starting at 1
        # check if index 1 + index 2 == target
        # return those two indexes
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


