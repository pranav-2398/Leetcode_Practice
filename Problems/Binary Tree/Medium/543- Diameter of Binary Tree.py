# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, 2 + left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return res
    
s = Solution()
root = TreeNode(4)
root.left = TreeNode(-7)
root.right = TreeNode(-3)
root.right.right = TreeNode(-3)
root.right.right.left = TreeNode(-4)
root.right.left = TreeNode(-9)
root.right.left.left = TreeNode(9)
root.right.left.left.left = TreeNode(6)
root.right.left.left.left.left = TreeNode(0)
root.right.left.left.left.left.right = TreeNode(-1)
root.right.left.left.left.right = TreeNode(6)
root.right.left.left.left.right.left = TreeNode(-4)
root.right.left.right = TreeNode(-7)
root.right.left.right.left = TreeNode(-6)
root.right.left.right.left.left = TreeNode(5)
root.right.left.right.right = TreeNode(-6)
root.right.left.right.right.left = TreeNode(9)
root.right.left.right.right.left.left = TreeNode(-2)

print(s.diameterOfBinaryTree(root))

        