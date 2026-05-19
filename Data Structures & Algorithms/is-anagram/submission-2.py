class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.countWord(s) == self.countWord(t)
    def countWord(self, word):
        output = {}

        for char in word:
            if char in output:
                output[char] += 1
            else:
                output[char] = 1
        return output