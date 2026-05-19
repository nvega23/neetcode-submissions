class Solution:
    def isValid(self, s: str) -> bool:
        tags = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []

        for char in s:
            if char in tags:
                if stack and stack[-1] == tags[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack

