import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res = float("inf")

        pairs = [] # ratio / quality

        for i in range(len(quality)):
            pairs.append(((wage[i] / quality[i]), quality[i]))
        pairs.sort(key = lambda x : x[0])

        maxheap = []
        total = 0
        for rate, q in pairs:
            heapq.heappush(maxheap, -q)
            total += q

            if len(maxheap) > k:
                total += heapq.heappop(maxheap)
            
            if len(maxheap) == k:
                res = min(res, total * rate)

        return res
        