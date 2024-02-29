# Definition for a binary tree node.

from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## DFS ########################################################
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        levels = defaultdict(list)
        mlevel = 0

        def dfs(node, level):
            if not node:
                return 
            
            levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            nonlocal mlevel
            mlevel = max(level, mlevel)

        dfs(root, 0)

        for level in range(mlevel + 1):
            if not level % 2:
                k = levels[level]
                for x in k:
                    if not x % 2:
                        return False

                for x, y in zip(k, k[1:]):
                    if x >= y:
                        return False
            else:
                k = levels[level]
                for x in k:
                    if x % 2:
                        return False

                for x, y in zip(k, k[1:]):
                    if x <= y:
                        return False
                    
        return True
####################################################################
    
### BFS #################################################################################################################
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        level = 0

        while queue:
            prev_val = None 

            for _ in range(len(queue)):
                node = queue.popleft()

                if (level % 2 == 0 and (node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val))) or \
                   (level % 2 == 1 and (node.val % 2 == 1 or (prev_val is not None and node.val >= prev_val))):
                    return False

                prev_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1
        return True
#########################################################################################################################

s = Solution()
# root = TreeNode(1)
# root.left = TreeNode(10)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(12)
# root.left.left.right = TreeNode(8)
# root.right = TreeNode(4)
# root.right.left = TreeNode(7)
# root.right.left.left = TreeNode(6)
# root.right.right = TreeNode(9)
# root.right.right.right = TreeNode(2)

root = TreeNode(5)
root.left = TreeNode(9)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right = TreeNode(1)
root.right.left = TreeNode(7)

print(s.isEvenOddTree(root))



