class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize an empty hash map
        # iterate over the nums array
            # check if the number is in the hash
                # if it is, increment + 1
            # return True
        # return False
        output = {}
        for num in nums:
            if num in output:
                output[num] += 1
                return True
            else:
                output[num] = 1
        return False

