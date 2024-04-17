from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

######## DFS ####################################################
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = ""
        level = float("inf")

        def dfs(node, depth, string):
            if not node:
                return 
            nonlocal level, res
            new_res = chr(97 + node.val) + string
            if not node.left and not node.right:
                if not res or new_res < res:
                    res = new_res
                    level = depth
            dfs(node.left, depth + 1, new_res)
            dfs(node.right, depth + 1, new_res)
        
        dfs(root, 0, "")
        return res
##################################################################
    
####### BFS #################################################################################################
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest_string = ""
        node_queue = deque()
        
        # Add root node to deque along with its value converted to a character
        node_queue.append([root, chr(root.val + ord('a'))])
        
        while node_queue:
            node, current_string = node_queue.popleft()
            
            if not node.left and not node.right:
                smallest_string = min(smallest_string, current_string) if smallest_string else current_string
            
            if node.left:
                node_queue.append([node.left, chr(node.left.val + ord('a')) + current_string])
            
            if node.right:
                node_queue.append([node.right, chr(node.right.val + ord('a')) + current_string])

        return smallest_string
###############################################################################################################