from typing import List

### MY SOLN (TIME EXCEED) ######################################################
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = []
#         for i in range(len(temperatures)):
#             k = i + 1
#             while k < len(temperatures) and temperatures[k] <= temperatures[i]:
#                 k += 1
            
#             if k == len(temperatures):
#                 res.append(0)
#             else:
#                 res.append(k - i)
        
#         return res
#################################################################################
    
### OPTIMISED SOLN ##############################################################
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair : (temp, index)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append((t, i))

        return res
##################################################################################
    
s = Solution()
# temp = [89,62,70,58,47,47,46,76,100,70]
temp = [73,74,75,71,69,72,76,73]
print(s.dailyTemperatures(temp))