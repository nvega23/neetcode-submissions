class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointer solution
        # we want a left and a right pointer
        # if left & right are not equal, then we have a unique value
        # if they are equal, then change the value to the right pointer
        fast = 1
        for slow in range(len(nums)):
            if nums[fast - 1] != nums[slow]:
                nums[fast] = nums[slow]
                fast += 1
        return fast

