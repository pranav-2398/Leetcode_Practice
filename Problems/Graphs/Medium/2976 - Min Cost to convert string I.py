import heapq
from typing import DefaultDict, List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = DefaultDict(list)

        for src, dist, curcost in zip(original, changed, cost):
            adj[src].append((curcost, dist))

        def dijkstra(src):
            heap = [(0, src)]
            costmap = {}

            while heap:
                cost, node = heapq.heappop(heap)
                if node in costmap:
                    continue
                costmap[node] = cost
                for neicost, nei in adj[node]:
                    heapq.heappush(heap, (cost + neicost, nei))
            return costmap

        mincostmaps = {c : dijkstra(c) for c in set(source)}
        res = 0
        for src, dst in zip(source, target):
            if dst not in mincostmaps[src]:
                return -1
            res += mincostmaps[src][dst]

        return res