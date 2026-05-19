class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the string
        # return a boolean when comparing both strings, one in reverse
        return sorted(s) == sorted(t[::-1])