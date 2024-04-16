from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        
        cur_depth = 1
        queue = deque([root])

        while queue:
            if cur_depth == depth - 1:
                break

            for _ in range(len(queue)):
                cur_node = queue.popleft()

                if cur_node.left:
                    queue.append(cur_node.left)

                if cur_node.right:
                    queue.append(cur_node.right)
                
            cur_depth += 1

        for node in queue:
            cur_left = node.left
            node.left = TreeNode(val, cur_left)

            cur_right = node.right
            node.right = TreeNode(val, None, cur_right)
        
        return root



s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left= TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)

s.addOneRow(root, 1, 2)

                

