from collections import defaultdict
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashmap = defaultdict(int)

        for l, r in edges:
            hashmap[l] += 1
            hashmap[r] += 1

        res = 1
        temp = -100

        for key in hashmap.keys():
            if hashmap[key] > temp:
                temp = hashmap[key]
                res = key
        
        return res
    
## GREEDY ########################################################################
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first_edge, second_edge = edges[0], edges[1]

        return first_edge[0] if first_edge[0] in second_edge else first_edge[1]
    
s = Solution()
edges = [[1,2],[2,3],[4,2]]
print(s.findCenter(edges))