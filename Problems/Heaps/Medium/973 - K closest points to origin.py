import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        dist = []
        for i in range(len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            dist.append((distance, i))
        heapq.heapify(dist)

        while k > 0:
            res.append(points[heapq.heappop(dist)[1]])
            k -= 1
        
        return res

s = Solution()
points = [[1,3],[-2,2]]
print(s.kClosest(points, 1))