
from collections import defaultdict
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

## MY SOLN (FAILED LAST CASE) #####################################
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        days = defaultdict(list)
        maxdays = 0

        intervals.sort(key = lambda x: x.start)
        days[0].append(intervals[0])

        for interval in intervals[1:]:
            insertflag = False
            for i in range(maxdays+1):
                if interval.start >= days[i][-1].end:
                    days[i].append(interval)
                    insertflag = True
                    break
            if not insertflag:
                days[maxdays + 1].append(interval)
                maxdays += 1
        
        return maxdays + 1
######################################################################

### OPTIMISED SOLN ###################################################
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0,0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(count, res)
        
        return res
########################################################################

s = Solution()
tempintervals=[
    (0,10),
    (10,20),
    (20,30),
    (30,40),
    (40,50),
    (50,60),
    (60,70),
    (70,80),
    (80,90),
    (90,100),
    (0,100),
    (10,90),
    (20,80),
    (30,70),
    (40,60),
    (50,50)
    ]
intervals = [Interval(x, y) for x, y in tempintervals]
print(s.minMeetingRooms(intervals))

