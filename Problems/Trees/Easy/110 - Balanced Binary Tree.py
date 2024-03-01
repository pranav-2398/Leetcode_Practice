# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            return float("inf") if abs(left - right) > 1 else 1 + max(left, right)  
        
        res = dfs(root)
        return False if res == float("inf") else True
        
s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(s.isBalanced(root))