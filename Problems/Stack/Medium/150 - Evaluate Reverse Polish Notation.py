from typing import List

#### MY SOLN ############################################################
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'*', '+', '-', '/'}

        for i in range(len(tokens)):
            if tokens[i] not in operations:
                stack.append(tokens[i])
            else:
                result = eval(f"int({stack[-2]}{tokens[i]}{stack[-1]})")
                stack.pop()
                stack.pop()
                stack.append(result)
        
        return int(stack[0])
############################################################################

s = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(s.evalRPN(tokens))
# print(eval("int(-6 / -132)"))
