from collections import defaultdict
from typing import List

#### MY SOLN #######################################################################
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dp = defaultdict(lambda: float('inf'))
        minval = float('inf')
        n = len(grid)

        for i in range(n):
            dp[(n - 1, i)] = grid[n - 1][i]
        
        for i in range(n - 2, -1, -1):
            for j in range(n):
                for k in range(n):
                    if k != j:
                        dp[(i, j)] = min(dp[(i, j)], grid[i][j] + dp[(i + 1, k)])
        
        for i in range(n):
            minval = min(minval, dp[(0, i)])
        
        return minval
######################################################################################       