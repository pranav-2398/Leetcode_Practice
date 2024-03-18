from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort balloons by their end position
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        end = points[0][1]
        
        for balloon in points:
            start, end_of_balloon = balloon
            # If the balloon starts after the current end point, it needs a new arrow
            if start > end:
                arrows += 1
                end = end_of_balloon  # Update the end point
        return arrows
        
    
s = Solution()
# points = [[10,16],[2,8],[1,6],[7,12]]
# points = [[1,2],[3,4],[5,6],[7,8]]
# points = [[1,2],[2,3],[3,4],[4,5]]
points = [[-1,1],[0,1],[2,3],[1,2]]
# points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
print(s.findMinArrowShots(points))