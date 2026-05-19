class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a count variable to keep track of how many times a num[i] + 1 == num[i+1]
        # use a set to eliminate all dups and sort the array and 
        # initialize an emtpy array
        # create a max_count = 1
        # count = 1
        # iterate over nums
        # check if num[i] + 1 == num[i+1]
            # count += 1
        # else
            # count = 1
            # max_count = max(count, max_count)
        # return max(count, max_count)
        if not nums:
            return 0
        count = 1
        max_count = 1
        nums = sorted(set(nums))
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        return max(max_count, count)