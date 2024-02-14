from collections import defaultdict

### MY SOLN ###########################################################
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = defaultdict(int)
#         dp[(m - 1, n - 1)] = 1

#         for j in range(n - 1, -1, -1):
#             for i in range(m - 1, -1, -1):
#                 dp[(i, j)] = dp[(i, j)] + dp[(i, j+1)] + dp[(i + 1, j)]

#         return dp[(0, 0)]
########################################################################

###### OPTIMISED MEMORY SOLN ###########################################
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
#########################################################################
s = Solution()
print(s.uniquePaths(3, 2))