class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = {}
        for num in nums:
            if num in output:
                output[num] += 1
                return True
            else:
                output[num] = 1
        return False