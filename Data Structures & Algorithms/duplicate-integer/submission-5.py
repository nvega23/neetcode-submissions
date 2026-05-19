class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate over array
        # initialize an empty hash map
        # check if the number is in the hash map
            # if so, hash[num] = 1
            # return true
        # else:
            # return false
        output = {}
        for num in nums:
            if num in output:
                return True
            else:
                output[num] = 1
        return False

