from typing import List

#####################################################################
# class Solution:
#     def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
#         res = [0] * len(arr)

#         i = len(arr) - 1
#         while i >= 0:
#             res[i] = arr[i]
#             j = i - 1
#             n = k - 1
#             #Backward
#             while n and j >=0:
#                 if arr[i] > arr[j]:
#                     res[j] = arr[i]
#                     j -= 1
#                     n -= 1
#                 else:
#                     break

#             if n:
#                 l = i + 1
#                 #Forward
#                 while n and l < len(arr):
#                     if arr[i] == res[l]:
#                         pass
#                     elif arr[i] > res[l]:
#                         res[l] = arr[i]
#                         l += 1
#                         n -= 1
#                     else:
#                         break
#             i = j
        
#         return sum(res)
##########################################################################

##### MEMOIZATION ########################################################
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            
            cur_max = 0
            res = 0
            for j in range(i, min(len(arr), i + k)):
                cur_max = max(cur_max, arr[j])
                window_size = j - i + 1
                res = max(res, dfs(j + 1) + cur_max * window_size)
            cache[i] = res
            return res
        
        return dfs(0)
############################################################################
    
#### DP SOLN ###############################################################
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * k
        dp[0] = arr[0]
        
        for i in range(1, len(arr)):
            cur_max = 0
            max_at_i = 0
            for j in range(i, i - k, -1):
                if j < 0:
                    break
                cur_max = max(cur_max, arr[j])
                window_size = i - j + 1
                cur_sum = cur_max * window_size
                sub_sum = dp[(j - 1) % k] if j > 0 else dp[-1]
                max_at_i = max(max_at_i, cur_sum + sub_sum)
            
            dp[i % k] = max_at_i
        
        return dp[(len(arr) - 1) % k]

s = Solution()
# arr = [1,15,7,9,2,5,10]
# arr = [1,4,1,5,7,3,6,1,9,9,3]
arr = [10, 9, 3, 2]
print(s.maxSumAfterPartitioning(arr, 2))
                    