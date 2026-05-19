class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            ")":"(",
            "]":"[",
            "}":"{",
        }

        stack = []

        for char in s:
            if char in chars:
                # true
                if stack and stack[-1] == chars[char]:
                    # [] and [)] == )
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack

