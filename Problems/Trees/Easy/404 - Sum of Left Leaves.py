from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node, left):
            nonlocal res
            if not node:
                return 0
            
            dfs(node.left, True)
            dfs(node.right, False)

            if not node.left and not node.right and left:
                res += node.val
        
        dfs(root, False)
        return res