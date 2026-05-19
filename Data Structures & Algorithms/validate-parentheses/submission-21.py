class Solution:
    def isValid(self, s: str) -> bool:
        pars = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack = []

        for char in s:
            if char in pars:
                if stack and stack[-1] == pars[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack

