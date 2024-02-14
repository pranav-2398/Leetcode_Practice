from collections import defaultdict
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = defaultdict(lambda: float('inf'))
        n = len(matrix)
        minval = float('inf')
        
        for i in range(n):
            dp[(n - 1, i)] = matrix[n - 1][i]

        for i in range(n - 2, -1, -1):
            for j in range(n):
                dp[(i, j)] = min(matrix[i][j] + dp[(i + 1, j)], 
                                 matrix[i][j] + dp[(i + 1, j - 1)], 
                                 matrix[i][j] + dp[(i + 1, j + 1)])
                
        for j in range(n):
            minval = min(minval, dp[(0, j)])
        return minval
        

s = Solution()
matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(s.minFallingPathSum(matrix))