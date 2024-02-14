from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(currstr, a, b):
            if len(currstr) == 2*n and currstr[-1] == ')':
                res.append(currstr)
            elif b <= a and a <= n:
                backtrack(currstr + '(', a+1, b)
                backtrack(currstr + ')', a, b+1)
        
        backtrack("(", 1, 0)
        return res
    
s = Solution()
print(s.generateParenthesis(3))