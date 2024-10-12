from typing import List

## MY SOLN (TLE) ############################################
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        groups = []
        for start, end in intervals:
            flag = True
            for group in groups:
                if start > group[1]:
                    group[1] = end
                    flag = False
                    break
            if flag:
                groups.append([start, end])
        return len(groups)
## OPTIMUM SOLN #############################################
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start =[]
        end = []
        for l, r in intervals:
            start.append(l)
            end.append(r)
        start.sort()
        end.sort()

        i,j = 0,0
        res =0
        groups = 0 
        while i < len(intervals):
            if start[i] <= end[j]:
                groups += 1
                i += 1
            else:
                groups -=1
                j += 1
            res = max(res, groups)
        return res
##############################################################