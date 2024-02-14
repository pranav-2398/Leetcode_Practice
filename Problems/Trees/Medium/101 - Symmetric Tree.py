# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def compare(left, right):
            
            if left and right:
                if left.val != right.val:
                    return False
                else:
                    return compare(left.right, right.left) and compare(left.left, right.right)
            else: 
                if left == right:
                    return True
                else:
                    return False
                
        return compare(root.left, root.right)
    
s = Solution()
t = TreeNode(9)
t.left = TreeNode(25)
t.right = TreeNode(25)
# t.left.left = TreeNode()
t.left.right = TreeNode(-95)
t.right.left = TreeNode(-95)
# t.right.right = TreeNode(3)
t.left.right.left = TreeNode(100)
t.right.left.right = TreeNode(-15)

print(s.isSymmetric(t))
