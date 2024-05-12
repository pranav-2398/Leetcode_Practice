from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        # res = [[0] * (n - 2)] * (n - 2)
        
        def findlargest(r, c):
            maxele = 0
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    maxele = max(maxele, grid[i][j])

            return maxele 
        
        for i in range(0, n - 2):
            for j in range(0, n - 2):
                res[i][j] = findlargest(i, j)

        return res