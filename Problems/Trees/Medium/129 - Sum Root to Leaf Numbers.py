from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

### MY SOLN ###############################################   
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node, string):
            if not node:
                return string
            string += str(node.val)
            if not node.left and not node.right:
                res.append(int(string))
                return 
            dfs(node.left, string)
            dfs(node.right, string)
        
        dfs(root, '')
        return sum(res)
############################################################

#### MEMORY OPTIMISED ######################################
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, path):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                ans += path * 10 + node.val
                return
            dfs(node.left, path * 10 + node.val)
            dfs(node.right, path * 10 + node.val)
        
        dfs(root, 0)
        return ans
##############################################################