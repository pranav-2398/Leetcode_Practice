from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        merged.append(newInterval)
        
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        
        return merged
    
s = Solution()
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
intervals = [[1,5]]
newInterval = [6,8]
# newInterval = [4,8]
print(s.insert(intervals, newInterval))