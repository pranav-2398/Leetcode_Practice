from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # Set first column
        for i in range(ROWS):
            if grid[i][0] == 0:
                # Flip row
                for j in range(COLS):
                    grid[i][j] = 0 if grid[i][j] else 1 

        # Optimize columns except first column
        for j in range(COLS):
            one_cnt = 0
            # Count zeros
            for i in range(ROWS):
                one_cnt += grid[i][j] 
            # Flip the column if more zeros for better score
            if one_cnt <  ROWS - one_cnt:
                for i in range(ROWS):
                    grid[i][j] = 0 if grid[i][j] else 1

        # Calculate the final score considering bit positions
        score = 0
        for i in range(ROWS):
            for j in range(COLS):
                # Left shift bit by place value of column to find column contribution
                score += grid[i][j] << (COLS - j - 1)

        # Return final result
        return score