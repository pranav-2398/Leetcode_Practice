from typing import List

## MY SOLN (TIME EXCESS) ###############################################
# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         res = []
#         nums.sort()

#         res.append([nums[-1]])
#         for i in range(len(nums) - 2, -1, -1):
#             flag = True
#             for j in range(len(res)):
#                 if not res[j][-1] % nums[i] or not nums[i] % res[j][-1]:
#                     val = res[j].copy()
#                     val.append(nums[i])
#                     res.append(val)
#                     # res[j].append(nums[i])
#                     flag = False
            
#             if flag:
#                 res.append([nums[i]])
    
#         res.sort(key=len)
#         return res[-1]
############################################################################

#### MEMOIZATION SOLN ######################################################
# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         cache = {}

#         def dfs(i, prev):
#             if i == len(nums):
#                 return []
#             if (i, prev) in cache:
#                 return cache[(i, prev)]
            
#             res = dfs(i + 1, prev) #skip nums[i]
#             if nums[i] % prev == 0:
#                 tmp = [nums[i]] + dfs(i + 1, nums[i]) #include nums[i]
#                 res = tmp if len(tmp) > len(res) else res
            
#             cache[(i, prev)] = res
#             return res
        
#         return dfs(0, 1)
##############################################################################

##############################################################################
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}

        def dfs(i):
            if i == len(nums):
                return []
            if i in cache:
                return cache[i]
            
            res = [nums[i]]

            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dfs(j)
                    if len(tmp) > len(res):
                        res = tmp
            
            cache[i] = res
            return res
        
        res = []
        for i in range(len(nums)):
            tmp = dfs(i)
            if len(tmp) > len(res):
                res = tmp

        return res
##################################################################################

#### DP SOLN #####################################################################
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[n] for n in nums] #dp[i] = longest start at i
        res = []

        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dp[j]
                    dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]
            res = dp[i] if len(dp[i]) > len(res) else res
        
        return res

        
s = Solution()
nums = [4, 8, 10, 240]
print(s.largestDivisibleSubset(nums))