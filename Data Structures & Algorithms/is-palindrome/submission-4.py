class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = []

        short = s.lower()
        for char in short:
            if char.isalnum():
                output.append(char)
        return "".join(output) == "".join(output)[::-1]

