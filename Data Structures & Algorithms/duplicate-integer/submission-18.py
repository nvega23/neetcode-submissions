class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize a hash map
        # iterate over the array
        # if that number is in the hashmap
        # return True
        # else, return False
        output = {}
        for num in nums:
            if num in output:
                return True
            output[num] = num
        return False

