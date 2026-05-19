class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = []
        for char in s.lower():
            joined = ' '.join(char)
            if joined.isalnum():
                # print(joined)
                output.append(joined)
        return "".join(output) == "".join(output[::-1])