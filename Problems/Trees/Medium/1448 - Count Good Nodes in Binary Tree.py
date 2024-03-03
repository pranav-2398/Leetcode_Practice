# Definition for a binary tree node.

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#### MY SOLN #####################################
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         res = 0
#         maxval = root.val

#         q = deque()

#         def dfs(node):
#             nonlocal res, maxval
#             if not node:
#                 return 
#             if node.val >= maxval:
#                 res += 1
#                 maxval = node.val
#             q.append(node)
#             dfs(node.left)
#             dfs(node.right)

#             if q:
#                 q.pop()
#                 maxval = -float("inf")
#                 for i in range(len(q)):
#                     maxval = max(maxval, q[i].val)
        
#         dfs(root)
#         return res
#######################################################

#### LESS CODE (SOLN) #################################
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)
#########################################################
    
s = Solution()
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.left.left = TreeNode(3)
# root.right = TreeNode(4)
# root.right.left = TreeNode(1)
# root.right.right = TreeNode(5)
root = TreeNode(2)
root.right = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(4)
print(s.goodNodes(root)) 