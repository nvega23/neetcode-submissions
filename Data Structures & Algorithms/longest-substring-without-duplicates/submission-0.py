class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newS = set()
# - create a set to track seen characters
        left, max_len = 0, 0
# - initialize left pointer and max_len to 0

# - for right in range(len(s)):
        for right in range(len(s)):
            while s[right] in newS:
                newS.remove(s[left])
                left += 1
            newS.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
#     - while s[right] is in the set:
#         - remove s[left] from the set
#         - move left pointer forward
#     - add s[right] to the set
#     - update max_len if current window (right - left + 1) is larger
# - return max_len