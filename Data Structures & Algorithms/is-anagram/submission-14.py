class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        an1, an2 = {}, {}
        for char in s:
            if char in an1:
                an1[char] += 1
            else:
                an1[char] = 1
        for char in t:
            if char in an2:
                an2[char] += 1
            else:
                an2[char] = 1
        return an1 == an2

