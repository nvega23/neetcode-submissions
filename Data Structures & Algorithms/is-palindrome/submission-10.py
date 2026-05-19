class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = []
        for char in s.lower():
            join = " ".join(char)
            if join.isalnum():
                output.append(join)
        return "".join(output) == "".join(output[::-1])