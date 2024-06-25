# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## MY SOLN ##########################################
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def dfs(node, value):
            if node.right:
                value = dfs(node.right, value)
            
            node.val += value

            if node.left:
                x = dfs(node.left, node.val)
                return max(node.left.val, x)
            
            return node.val
        
        dfs(root, 0)
        return root

## ITERATIVE SOLN ###################################
# class Solution:
#     def bstToGst(self, root: TreeNode) -> TreeNode:
#         node_sum = 0
#         st = []
#         node = root

#         while st or node is not None:

#             while node is not None:
#                 st.append(node)
#                 node = node.right
#             # Store the top value of stack in node and pop it.
#             node = st.pop()

#             # Update value of node.
#             node_sum += node.val
#             node.val = node_sum

#             # Move to the left child of node.
#             node = node.left
#         return root
################################################################

s = Solution()
# root = TreeNode(4)
# root.right = TreeNode(6)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(7)
# root.right.right.right = TreeNode(8)
# root.left = TreeNode(1)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(2)
# root.left.right.right = TreeNode(3)

root = TreeNode(6)
root.right = TreeNode(10)
root.right.left = TreeNode(8)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(9)
root.right.right = TreeNode(12)
root.right.right.left = TreeNode(11)
root.right.right.right = TreeNode(13)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.left.right = TreeNode(1)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

s.bstToGst(root)

