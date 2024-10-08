from collections import defaultdict
import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])
        
        heap = [(-1, start_node)]
        visit = set()

        while heap:
            prob, cur = heapq.heappop(heap)
            visit.add(cur)

            if cur == end_node:
                return -prob

            for nei, edgeprob in adj[cur]:
                if nei not in visit:
                    heapq.heappush(heap, (prob * edgeprob, nei ))

        return 0