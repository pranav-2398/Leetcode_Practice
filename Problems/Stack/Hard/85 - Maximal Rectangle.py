from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ROWS , COLS = len(matrix), len(matrix[0])
        currow = list(map(lambda x: int(x),matrix[0]))
        maxans = self.largestRectangleArea(currow)

        for i in range(1, ROWS):
            for j in range(COLS):
                if int(matrix[i][j]) == 1:
                    currow[j] += 1
                else:
                    currow[j] = 0
        
            curans = self.largestRectangleArea(currow)
            maxans = max(maxans, curans)
        
        return maxans

    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair : (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

s = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(s.maximalRectangle(matrix))
