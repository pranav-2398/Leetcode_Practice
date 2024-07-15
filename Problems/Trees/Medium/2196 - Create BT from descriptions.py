from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodemap = {}
        visited = set()
        for parent, child, isleft in descriptions:
            visited.add(child)
            if parent not in nodemap:
                nodemap[parent] = TreeNode(parent)
            if child not in nodemap:
                nodemap[child] = TreeNode(child)
            if isleft:
                nodemap[parent].left = nodemap[child]
            else:
                nodemap[parent].right = nodemap[child]
        
        for p, c, l in descriptions:
            if p not in visited:
                return nodemap[p]
    
descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
s = Solution()
root = s.createBinaryTree(descriptions)