class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        output = []

        for char in s:
            if char in chars:
                if output and output[-1] == chars[char]:
                    output.pop()
                else:
                    return False
            else:
                output.append(char)
        return not output