from collections import defaultdict, deque
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        q = deque([1])
        curtime = 0
        res = -1
        visittimes = defaultdict(list)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == n:
                    if res != -1:
                        return curtime
                    res = curtime
                for nei in adj[node]:
                    neitime = visittimes[nei] 
                    if len(neitime) == 0 or (len(neitime) == 1 and neitime[0] != curtime) :
                        q.append(nei)
                        neitime.append(curtime)

            if (curtime // change) % 2 == 1:
                curtime += change - (curtime % change) 
            curtime += time