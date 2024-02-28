# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    ####### RECURSIVE SOLN ###############################################
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     result = []

    #     def helper(node, result):
    #         if not node:
    #             return 
    #         else:
    #             if node.left:
    #             # result.append(node.left.val)
    #                 helper(node.left, result)
            
    #             result.append(node.val)
    #             if node.right:
    #                 # result.append(node.right.val)
    #                 helper(node.right, result)

    #     helper(root, result)

    #     return result
    ########################################################################

    ###### ITERATIVE SOLN ##################################################

    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     result = []
    #     queue = []
    #     popped = {}

    #     queue.append(root)

    #     while len(queue):
    #         if queue[-1].left and queue[-1].left.val not in popped:
    #             queue.append(queue[-1].left)
    #         else:
    #             result.append(queue[-1].val)
                
    #             if queue[-1].right:
    #                 temp = queue.pop()
    #                 queue.append(temp.right)
    #                 popped[temp.val] = 1
    #             else:
    #                 popped[queue.pop().val] = 1

    #     return result
    
    ######################################################################

    ######### ITERATIVE SOLN 2 ###########################################

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
    
    ########################################################################

s = Solution()

t = TreeNode(37)
t.left = TreeNode(-34)
t.left.right = TreeNode(-100)
t.right = TreeNode(-48)
t.right.left = TreeNode(-100)
t.right.right = TreeNode(48)
t.right.right.left = TreeNode(-54)
t.right.right.left.left = TreeNode(-71)
t.right.right.left.right = TreeNode(-22)
t.right.right.left.right.right = TreeNode(8)

# t= TreeNode(1)

print(s.inorderTraversal(t))


