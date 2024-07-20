from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ROWS, COLS = len(rowSum), len(colSum)

        res = [[0] * COLS for r in range(ROWS)]

        for r in range(ROWS):
            res[r][0] = rowSum[r]

        for c in range(COLS):
            curcolSum = 0
            for r in range(ROWS):
                curcolSum += res[r][c]

            r = 0
            while curcolSum > colSum[c]:
                diff = curcolSum - colSum[c]
                maxshift = min(res[r][c], diff)

                res[r][c] -= maxshift
                res[r][c + 1] += maxshift
                curcolSum -= maxshift
                r += 1
        return res
