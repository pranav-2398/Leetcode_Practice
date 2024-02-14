from typing import List

##### MY SOLN ##############################################################
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix) - 1
#         #Swapping Elements
#         for row in matrix:
#             l, r = 0, len(row) - 1
#             while l < r:
#                 row[l], row[r] = row[r], row[l]
#                 l += 1
#                 r -= 1
        
#         l = n
#         #Swapping Transpose Elements
#         for i in range(n + 1):
#             k = n
#             for j in range(n - i + 1):
#                 matrix[i][j] , matrix[k][l] = matrix[k][l], matrix[i][j] 
#                 if not k - i :
#                     l -= 1
#                 k -= 1
################################################################################
                
### OPTIMISED SOLN #############################################################
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                #save Topleft
                topleft = matrix[top][l + i]

                #move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                #move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                #move top left into top right
                matrix[top + i][r] = topleft
            
            r -= 1
            l += 1

#################################################################################

s = Solution()
matrix= [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(matrix)
print(matrix)
        
