from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj_list = defaultdict(list)
        for e1, e2, w in edges:
            adj_list[e1].append((e2, w))
            adj_list[e2].append((e1, w))

        def bfs(src):
            heap = [(0, src)]
            visit = set()
            
            while heap:
                dist, node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                for nei, dist2 in adj_list[node]:
                    neidist = dist + dist2
                    if neidist <= distanceThreshold:
                        heapq.heappush(heap, (neidist, nei))
            
            return len(visit) - 1

        res, mincount = -1, n
        for src in range(n):
            count = bfs(src)
            if count <= mincount:
                res, mincount = src, count
        return res