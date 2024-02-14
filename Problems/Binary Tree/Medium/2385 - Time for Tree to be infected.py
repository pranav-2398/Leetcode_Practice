# Definition for a binary tree node.

from typing import Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        matrix = defaultdict(list)
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                matrix[node.val].append(node.left.val)
                matrix[node.left.val].append(node.val)
            
            if node.right:
                queue.append(node.right)
                matrix[node.val].append(node.right.val)
                matrix[node.right.val].append(node.val)

        queue = deque()
        queue.append((start, 0))
        visited = set()
        visited.add(start)

        while queue:
            node, time = queue.popleft()

            for vals in matrix[node]:
                if vals not in visited:
                    queue.append((vals, time + 1))
                    visited.add(vals)
        
        return time
