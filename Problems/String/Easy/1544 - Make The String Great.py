class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) <= 1:
            return s
        stack = [s[0]]
        i = 1
        while i < len(s):
            if stack and s[i].lower() == stack[-1].lower() and abs(ord(s[i]) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)


s = Solution()
print(s.makeGood("abBAcC"))