class Solution:
    def minOperations(self, s: str) -> int:
        stack = []
        counter = 0
        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char == stack[-1]:
                    counter += 1
                    stack.pop()
                else:
                    stack.append(char)
            
        return counter

    
s = Solution()
print(s.minOperations('1111'))
            