class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize a hash map
        # iterate over the array
        # if the number is in the hash map
        # increment the count by 1
        # return True
        # if the number is not in the hash map
        # initialize the number to 1
        # return False
        output = {}
        for num in nums:
            if num in output:
                output[num] += 1
                return True
            else:
                output[num] = 1
        return False