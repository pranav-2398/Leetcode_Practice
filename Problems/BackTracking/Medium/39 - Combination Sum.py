from typing import List

######### MY SOLN ###################################################################
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []

#         candidates.sort()

#         def dfs(i, diff, subset):
#             if not diff:
#                 res.append(subset)
#             elif diff < 0:
#                 return 
            
#             for k in range(i, len(candidates)):
#                 if diff - candidates[k] >= 0:
#                     temp = subset.copy()
#                     temp.append(candidates[k])
#                     dfs(k, diff - candidates[k], temp)
#                 else:
#                     break
            
#         for i in range(len(candidates)):
#             dfs(i, target - candidates[i], [candidates[i]])
        
#         return res
#####################################################################################

###### LESS CODE SOLN ###############################################################
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res
######################################################################################
s = Solution()
candidates = [2,3,6,7]
target = 7
print(s.combinationSum(candidates, target))
