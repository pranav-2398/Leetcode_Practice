from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        res = 0
        for i in range(k):
            if not i:
                res += happiness[i]
            else:
                res += happiness[i] - i if happiness[i] - i > 0 else 0
        
        return res