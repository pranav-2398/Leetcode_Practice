# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

### MY SOLN ############################################################################
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def helper(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return helper(node1.left, node2.left) and helper(node1.right, node2.right)
    
        return helper(p, q)
########################################################################################

### MY SOLN (W/O Helper definition) ####################################################  
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         if p.val != q.val:
#             return False
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#########################################################################################
    
s = Solution()
p = TreeNode(1)
q = TreeNode(1)
p.left = TreeNode(2)
q.left = TreeNode(2)
p.right = TreeNode(3)
q.right = TreeNode(3)

print(s.isSameTree(p, q))