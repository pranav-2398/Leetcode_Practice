# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []
        
        def getleafnodes(root, res):
            if not root.left and not root.right:
                res.append(root.val)
            elif root.left:
                getleafnodes(root.left, res)
            elif root.right:
                getleafnodes(root.right, res)

        getleafnodes(root1, res1)
        getleafnodes(root2, res2)

        return res1 == res2
            