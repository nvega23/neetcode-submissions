class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        output = {}
        output2 = {}

        for char in s:
            if char in output:
                output[char] += 1
            else:
                output[char] = 1
        for char2 in t:
            if char2 in output2:
                output2[char2] += 1
            else:
                output2[char2] = 1
        return output == output2