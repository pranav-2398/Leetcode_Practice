from typing import List
import heapq


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        heap = []
        for i, e in enumerate(arr):
            heap.append((e, i))
        
        heapq.heapify(heap)
        rank = 0
        prev = None
        res = [0] * len(arr)
        while heap:
            e, i = heapq.heappop(heap)
            if e != prev:
                rank += 1
            res[i] = rank
            prev = e
        return res
    
s = Solution()
arr = [37,12,28,9,100,56,80,5,12]
print(s.arrayRankTransform(arr))