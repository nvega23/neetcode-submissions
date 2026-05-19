class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output = {}
        maxp = 0
        l = 0
        res = 0
        for r in range(len(s)):
            output[s[r]] = 1 + output.get(s[r], 0)
            maxp = max(output[s[r]], maxp)
            while (r - l + 1) - maxp > k:
                output[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res