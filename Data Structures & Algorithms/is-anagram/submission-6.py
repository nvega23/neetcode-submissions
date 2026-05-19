class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        news = sorted(s)
        newt = sorted(t)
        return news == newt