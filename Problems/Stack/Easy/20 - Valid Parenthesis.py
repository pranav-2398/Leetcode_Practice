class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        open_index = close_index = 0
        stack = []
        symbols = {"}":"{", ")":"(", "]":"["}

        for char in s:
            if char in ("(", "{", "["):
                stack.append(char)
            elif stack and stack[-1] == symbols[char]:
                stack.pop()
            else:
                return False

        return True if not stack else False