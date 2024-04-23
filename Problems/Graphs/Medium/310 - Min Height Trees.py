from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        edge_cnt = {}
        leaves = deque()
        for src, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(src)
            edge_cnt[src] = len(neighbors)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1

                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)

s = Solution()
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
n = 6
print(s.findMinHeightTrees(n, edges))