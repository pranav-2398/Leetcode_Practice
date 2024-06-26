from typing import List


class UF:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)

        if p1 == p2:
            return 0
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        self.n -= 1
        return 1
    
    def isConnected(self):
        return self.n == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UF(n), UF(n)
        cnt = 0 #No of edges we have to keep

        for t, src, dst in edges:
            if t == 3:
                cnt += (alice.union(src, dst) | bob.union(src, dst))

        for t, src, dst in edges:
            if t == 1:
                cnt += alice.union(src, dst)
            elif t == 2:
                cnt += bob.union(src, dst)

        if bob.isConnected() and alice.isConnected():
            return len(edges) - cnt
        return -1
