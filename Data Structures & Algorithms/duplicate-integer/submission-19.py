class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize a hashmap
        # iterate over array nums
        # check if the number is in the hashmap
            # if not, then we will add it to the hashmap
            # if it is, we will return True
        # otherwise we will return False
        output = {}
        for num in nums:
            if num in output:
                return True
            else:
                output[num] = num
        return False

