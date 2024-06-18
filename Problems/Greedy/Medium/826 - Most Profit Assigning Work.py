from collections import deque
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ziped = list(zip(difficulty, profit))
        ziped.sort()

        worker.sort()

        queue = deque(ziped)
        res = 0
        maxprofit = 0
        for i in range(len(worker)):
            while len(queue) > 0 and queue[0][0] <= worker[i]:
                d, p = queue.popleft()
                maxprofit = max(maxprofit, p)
            
            res += maxprofit
        
        return res

s = Solution()
difficulty = [13,37,58]
profit = [4,90,96]
worker = [34,73,45]
print(s.maxProfitAssignment(difficulty, profit, worker))
