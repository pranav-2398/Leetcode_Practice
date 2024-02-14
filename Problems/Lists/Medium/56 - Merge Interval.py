from typing import List

######### MY SOLN ###################################################################
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        res.append(intervals[0])

        j = 0
        for i in range(1, len(intervals)):
            if (res[-1][1] >= intervals[i][0] and res[-1][1] <= intervals[i][1]) or (
                res[-1][1] >= intervals[i][0] and res[-1][1] >= intervals[i][1]
            ):
                res[j][0] = min(res[j][0], intervals[i][0])
                res[j][1] = max(intervals[i][1], res[j][1])
            else:
                res.append(intervals[i])
                j += 1
        
        return res
#######################################################################################
    
### OPTIMISED SOLN ####################################################################
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        res.append(intervals[0])

        for start, end in intervals[1:]:
            lastend = res[-1][1]

            if start <= lastend:
                res[-1][1] = max(lastend, end)
            else:
                res.append([start, end])

        return res    
##########################################################################################
    
s = Solution()
# nums = [[1,3],[2,6],[8,10],[15,18]]
# nums = [[1,4],[4,5]]
nums = [[1,4],[0,2],[3,5]]
print(s.merge(nums))
