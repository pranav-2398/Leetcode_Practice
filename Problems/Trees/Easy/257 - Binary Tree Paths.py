from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def dfs(node, string):
            if not node.left and not node.right:
                res.append(string)
            
            if node.left:
                dfs(node.left, string + '->' + str(node.left.val))
            if node.right:
                dfs(node.right, string + '->' + str(node.right.val))
        
        dfs(root, str(root.val))

        return res

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)

print(s.binaryTreePaths(root))
