from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        row = points[0]
        
        for r in range(1, rows):
            nextrow = points[r].copy()
            left, right = [0] * cols, [0] * cols
            
            left[0] = row[0]

            for c in range(1, cols):
                left[c] = max(row[c], left[c - 1] - 1)

            right[-1] = row[-1]
            for c in range(cols - 2, -1, -1):
                right[c] = max(row[c], right[c + 1] - 1)

            for c in range(cols):
                nextrow[c] += max(left[c], right[c])
            
            row = nextrow
        
        return max(row)


points = [[1,5],[2,3],[4,2]]
s = Solution()
print(s.maxPoints(points))