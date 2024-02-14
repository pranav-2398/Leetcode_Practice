# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

############# ORIGINAL SOLUTION ################################
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:

#         if root:
#             if not root.left and not root.right:
#                 return 1
#         else:
#             return 0

#         def helper(root):
#             left_length = 1
#             right_length = 1
            
#             if not root:
#                 return 1
#             if root.left:
#                 left_length += helper(root.left)
#             if root.right:
#                 right_length += helper(root.right)
                
#             return max(left_length, right_length)
        
#         return helper(root)
########################################################################

###### RECURSIVE DFS ########################################################

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
#############################################################################
    
######## ITERATIVE DFS ######################################################

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        
        return res

###############################################################################

s= Solution()
t = TreeNode(1)
t.right = TreeNode(2)
print(s.maxDepth(t))
            
            
