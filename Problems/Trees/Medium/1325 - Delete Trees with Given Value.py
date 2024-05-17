from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            return None if node.val == target and (not node.left and not node.right) else node
        
        return dfs(root)
        
s = Solution()
root = TreeNode(1)
root.left = TreeNode(1)
root.right= TreeNode(1)

s.removeLeafNodes(root, 1)