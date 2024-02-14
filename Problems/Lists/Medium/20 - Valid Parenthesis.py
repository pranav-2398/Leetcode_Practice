class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []
        
        symbols = {']':'[', '}':'{', ')':'('}

        for char in s:
            if char in ('(', '{', '['):
                char_stack.append(char)
            else:
                if (not char_stack and char in symbols.keys()) or (char_stack and char_stack[-1] != symbols.get(char)):
                    return False
                else:
                    char_stack.pop()
            
        if not char_stack:
            return True
        
        return False

soln = Solution()
print(soln.isValid('(]'))
             