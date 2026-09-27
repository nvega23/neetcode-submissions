class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        output = {}
        output2 = {}

        for char in s:
            if char in output:
                output[char] += 1
            else:
                output[char] = 1
        for char in t:
            if char in output2:
                output2[char] += 1
            else:
                output2[char] = 1
        
        return output == output2