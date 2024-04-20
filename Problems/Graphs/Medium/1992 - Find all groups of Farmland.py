from typing import List

### MY SOLN ##################################################################
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(land), len(land[0])
        res = []

        def dfs(i, j, pos):
            if i < 0 or i == ROWS or j < 0 or j == COLS or land[i][j] == 0:
                return 
            land[i][j] = 0
            if (pos[0] > i) or (pos[0] == i and pos[1] > j):
                pos[0], pos[1] = i, j
            if (pos[2] < i) or (pos[2] == i and pos[3] < j):
                pos[2], pos[3] = i, j
             
            dfs(i + 1, j, pos)
            dfs(i, j + 1, pos)
            dfs(i - 1, j, pos)
            dfs(i, j - 1, pos)

            return pos
        
        for i in range(ROWS):
            for j in range(COLS):
                if land[i][j] == 1:
                    pos = dfs(i, j, [float("inf"), float("inf"), -1, -1])
                    res.append(pos)

        return res
############################################################################

s = Solution()
land = [[1,0,0],[0,1,1],[0,1,1]]
print(s.findFarmland(land))

            