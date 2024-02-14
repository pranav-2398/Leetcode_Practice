# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def preorder(root):
            res = 0
            if root:
                if low <= root.val <= high:
                    res += root.val
                    res += preorder(root.left)
                    res += preorder(root.right)
                elif root.val < low:
                    res += preorder(root.right)
                else:
                    res += preorder(root.left)
                return res
            else:
                return 0
        
        return preorder(root)

