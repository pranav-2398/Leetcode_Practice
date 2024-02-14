from typing import List

### ORIGINAL SOLN WHICH FAILED #######################################
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         res = 0
#         i = 0
#         while i < len(height):
#             j = i + 1
#             sumx = 0
#             while j <= len(height) - 1 and height[i] >  height[j] + 1:
#                 sumx += height[i] - height[j]
#                 res += height[i] - height[j] 
#                 j += 1
            
#             if j == len(height) and  height[i] > height[j - 1]:
#                 res -= sumx
#                 j = i + 1
            
#             i = j
#         return res
#########################################################################

######## SOLN ###########################################################
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res

###########################################################################   

s = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,3]
print(s.trap(height))
            
