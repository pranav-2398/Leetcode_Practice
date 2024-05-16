from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        mapping = {
            0: False,
            1: True,
            2: '|',
            3: '&'
        }

        def dfs(node):
            if node.left and node.right:
                left = dfs(node.left)
                right = dfs(node.right)
                return eval(f"{mapping[left]} {mapping[node.val]} {mapping[right]}")
            else:
                return mapping[node.val]
        
        return dfs(root)



