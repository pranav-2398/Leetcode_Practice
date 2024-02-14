from typing import List

#### MY SOLN #############################################
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []

#         for num in nums:
#             for i in range(len(res)):
#                 temp = res[i].copy()
#                 temp.append(num)
#                 res.append(temp)
#             res.append([num])
        
#         res.append([])
#         return res
############################################################

### BACKTRACKING SOLN ######################################
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            #decision not to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return res
#############################################################

s = Solution()
nums = [1, 2, 3]
print(s.subsets(nums))
            
            