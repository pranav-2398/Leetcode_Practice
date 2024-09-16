from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        
        def time_to_min(t):
            h, m = map(int, t.split(":"))
            return h * 60 + m
        
        res = 24 * 60 - time_to_min(timePoints[-1]) + time_to_min(timePoints[0])
        for i in range(len(timePoints) - 1):
            cur = time_to_min(timePoints[i + 1])
            prev = time_to_min(timePoints[i])
            res = min(res, cur - prev)
        
        return res