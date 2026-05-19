class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # sliding window
        # If I am on the first index, multiply all except for the first index
        # else, mult the left side and the right side
        # grab the ledt and right side
        output = []
        for i in range(len(nums)):
            left = nums[:i]
            right = nums[i+1:] 
            prod = 1

            for num in left + right:
                prod *= num
            output.append(prod)
        return output
