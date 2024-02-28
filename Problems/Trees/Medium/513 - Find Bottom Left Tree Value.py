# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
##### MY SOLN ######################################################
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level):
            left = (node, level)
            right = (node, level)
            
            if node.left:
                left = dfs(node.left, level + 1)
            if node.right:
                right = dfs(node.right, level + 1)

            if left[1] >= right[1]:
                return left
            else:
                return right
                
        leftval = dfs(root, 0)
        return leftval[0].val
#######################################################################
    
### OPTIMISED SOLN (LESS CODE) ########################################
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        d = deque(root)
        while d:
            node = d.popleft()
            if node.right:
                d.append(node.right)
            if node.left:
                d.append(node.left)
        return node.val
#######################################################################
    
s = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(s.findBottomLeftValue(root))


