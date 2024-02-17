import heapq
from typing import List

###MY SOLN (TIME EXCESS)##################################################################################
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        def checkbuild(start,bricks, ladders):
            res = start
            res1 = res2 = 0
            if start == len(heights) - 1:
                return start
            if heights[start] > heights[start + 1]:
                res = checkbuild(start + 1, bricks, ladders)
            else:
                if bricks and heights[start + 1] - heights[start] <= bricks :
                    res1 = checkbuild(start + 1, bricks - (heights[start + 1] - heights[start]), ladders)
                if ladders:
                    res2 = checkbuild(start + 1, bricks, ladders - 1)
            res = max(res, res1, res2)
            return res
        
        return checkbuild(0, bricks, ladders)
##########################################################################################################

### OPTIMISED SOLN #######################################################################################
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = [] #max heap of bricks

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            bricks -= diff
            heapq.heappush(heap, -diff)

            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(heap)
            
        return len(heights) - 1

############################################################################################################


s = Solution()
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
# heights = [4,12,2,7,3,18,20,3,19]
# bricks = 10
# ladders = 2
# heights = [14,3,19,3]
# bricks = 17
# ladders = 0

print(s.furthestBuilding(heights, bricks, ladders))
