import bisect
from typing import List

######### MY SOLN ###############################################################################
# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         nums = []

#         for l in range(len(startTime)):
#             nums.append((startTime[l], endTime[l], l))
        
#         nums.sort()

#         dp = [None] * len(nums)

#         for i in range(len(nums)-1, -1, -1):
#             dp[i]= profit[nums[i][2]]
#             for j in range(i+1, len(nums)):
#                 if nums[i][1] <= nums[j][0]:
#                     dp[i] = max(dp[i], profit[nums[i][2]] + dp[j])

#         return max(dp)
#################################################################################################  

#### NEETCODE SOLN #############################################################################
    
# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         intervals = sorted(zip(startTime, endTime, profit))
#         cache = {}

#         def dfs(i):
#             if i == len(intervals):
#                 return 0
#             if i in cache:
#                 return cache[i]

#             res = dfs(i + 1)

#             j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
#             cache[i] = res = max(res, intervals[i][2] + dfs(j))
#             return res
        
#         return dfs(0)
################################################################################################

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            res = dfs(i + 1)

            j = i + 1
            
            while j < len(intervals):
                if intervals[i][1] <= intervals[j][0]:
                    break
                j += 1
            
            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res
        
        return dfs(0)
    

s = Solution()
st = [1,2,3,3]
et = [3,4,5,6]
pr = [50,10,40,70]

print(s.jobScheduling(st, et, pr))