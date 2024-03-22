import heapq
from typing import List

### MY SOLN (TLE) ########################################################################
# class Solution:
#     def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
#         intervals = [[start, end, end - start + 1] for start, end in intervals]
#         intervals.sort(key = lambda x: (x[2], x[0]))

#         res = []
#         for num in queries:
#             flag = False
#             for i in intervals:
#                 if i[0] <= num <= i[1]:
#                     res.append(i[2])
#                     flag = True
#                     break
#             if not flag:
#                 res.append(-1)
#         return res
############################################################################################

#### OPTIMISED SOLN ########################################################################
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        minheap = []
        res, i = {}, 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minheap, (r - l + 1, r))
                i += 1
            
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            res[q] = minheap[0][0] if minheap else -1

        return [res[q] for q in queries]

############################################################################################

s = Solution()
# intervals = [[1,4],[2,4],[3,6],[4,4]]
intervals = [[2,3],[2,5],[1,8],[20,25]]
queries = [2,19,5,22]
# queries = [2,3,4,5]
print(s.minInterval(intervals, queries))
