#Done on Neetcode.io

from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key = lambda x: x.start)

        prevEnd = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < prevEnd:
                return False
            else:
                prevEnd = max(interval.end, prevEnd)
        
        return True

intervals = [Interval(0,30),Interval(5,10),Interval(15,20)]
s = Solution()
print(s.canAttendMeetings(intervals))