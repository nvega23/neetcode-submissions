class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = []

        for char in s.lower():
            if char.isalnum():
                output.append(char)
        return ''.join(output) == ''.join(output[::-1])