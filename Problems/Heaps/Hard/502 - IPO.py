import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(capital[i], profits[i]) for i in range(len(profits))]
        heapq.heapify(minCapital)
        res = w
        prev = -1

        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)
            
            if not maxProfit:
                break
            
            w+= -heapq.heappop(maxProfit)
        
        return w
    
s = Solution()
k = 1
w = 2
profits = [1, 2, 3]
capital = [1, 1, 2]
print(s.findMaximizedCapital(k, w, profits, capital))