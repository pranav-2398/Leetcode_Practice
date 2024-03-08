# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float("inf")

        def dfs(node, maxval):
            nonlocal res
            if not node:
                return -float("inf")
            left = dfs(node.left, maxval)
            right = dfs(node.right, maxval)

            maxval = max(maxval, node.val, node.val + max(left, right))
            res = max(res, maxval, node.val + left + right)

            return maxval
        
        dfs(root, -float("inf"))
        return res
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)