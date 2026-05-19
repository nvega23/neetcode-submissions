class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make everything lowercased
        # ensure that all characters are letters
        # join everything together
        # return the joined string and compare to the same joined string but in reverse
        low = s.lower()
        output = []
        for char in low:
            if char.isalnum():
                joined = ''.join(char)
                output.append(joined)
        return output == output[::-1]