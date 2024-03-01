# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

########### MY SOLN ####################################################################       
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return False
            
            check = False
            if node.val == subRoot.val:
                check = equality(node, subRoot)

            left = dfs(node.left)
            right = dfs(node.right)

            return check or left or right
        
        def equality(p, q):
            if not p and not q:
                return True
            if (not p or not q):
                return False
            if p.val != q.val:
                return False
            
            return equality(p.left, q.left) and equality(p.right, q.right)
        
        return dfs(root)
###########################################################################################

### Less Code Soln ########################################################################
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot):
            return True
        
        return (
            self.isSubtree(root.left, subRoot.left) 
            or self.isSubtree(root.right, subRoot.right)
        )
    
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False
##########################################################################################
   
s = Solution()
root = TreeNode(3)
root.right = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(s.isSubtree(root, subRoot))