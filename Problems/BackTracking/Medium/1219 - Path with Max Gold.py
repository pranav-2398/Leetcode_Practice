from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def backtrack(r, c, visited):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or not grid[r][c] or (r,c) in visited:
                return 0
            visited.add((r,c))
            res = grid[r][c]
            maxgold =  max(
                backtrack(r, c - 1, visited),
                backtrack(r, c + 1, visited), 
                backtrack(r - 1, c, visited),
                backtrack(r + 1, c, visited)
            )
            visited.remove((r, c))
            return res + maxgold

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, backtrack(i, j, set()))

        return res