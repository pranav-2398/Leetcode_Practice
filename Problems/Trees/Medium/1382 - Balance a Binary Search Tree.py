# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arrtree = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            arrtree.append(node.val)

            inorder(node.right)
        
        def construct_bst(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            node = TreeNode(arrtree[mid])
            node.left = construct_bst(l, mid - 1)
            node.right = construct_bst(mid + 1, r)

            return node
        
        inorder(root)
        return construct_bst(0, len(arrtree) - 1)