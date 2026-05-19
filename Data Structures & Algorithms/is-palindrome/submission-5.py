class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = s.lower()
        output = []
        for char in low:
            if char.isalnum():
                output.append(char)
        return ''.join(output) == ''.join(output)[::-1]