from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return (0, 0)
            
            left = dfs(node.left)
            right = dfs(node.right)

            coin_transfer = node.val - 1 + left[0] + right[0]
            moves = abs(coin_transfer) + abs(left[1]) + abs(right[1])

            return (coin_transfer, moves)
        
        value = dfs(root)
        
        return value[1]
    
s = Solution()
root = TreeNode(3)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.left.left = TreeNode(0)
root.left.right = TreeNode(0)
root.right = TreeNode(1)
root.right.left = TreeNode(4)
root.right.right = TreeNode(0)

print(s.distributeCoins(root))