from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def magic(r, c):
            values = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] in values or not(1 <= grid[i][j] <= 9):
                        return 0
                    values.add(grid[i][j])
            
            for i in range(r, r + 3):
                if sum(grid[i][c:c + 3]) != 15:
                    return 0
            
            for j in range(c, c + 3):
                if (grid[r][j] + grid[r + 1][j] + grid[r + 2][j]) != 15:
                    return 0
            
            if (
                grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15 or
                grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15
                ):
                return 0
            
            return 1
            
        res = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                res += magic(r,c)

        return res