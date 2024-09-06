from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m + n)
        missing = total - sum(rolls)

        if missing > 6 * n  or missing < n:
            return []
        
        res = []

        while n:
            dice = min(6, missing - n + 1)
            missing -= dice
            res.append(dice)
            n -= 1

        return res