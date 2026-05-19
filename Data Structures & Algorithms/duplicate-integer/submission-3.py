class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Count all numbers
        # return true if number was seen more than once
        output = {}

        for num in nums:
            if num in output:
                return True
            else:
                output[num] = 1
        return False