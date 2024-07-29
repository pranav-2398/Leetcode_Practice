from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for m in range(1, len(rating) - 1):
            leftsmaller = rightlarger = 0

            for i in range(m):
                if rating[i] < rating[m]:
                    leftsmaller += 1
            
            for i in range(m + 1, len(rating)):
                if rating[i] > rating[m]:
                    rightlarger += 1
        
            res += leftsmaller * rightlarger #count ascend
            leftlarger = m - leftsmaller
            rightsmaller = len(rating) - m - 1 - rightlarger
            res += leftlarger * rightsmaller
        
        return res