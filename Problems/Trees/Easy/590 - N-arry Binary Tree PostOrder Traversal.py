from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

## RECURSIVE SOLN#######################################
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(node):
            if not node:
                return 
            for child in node.children:
                helper(child)
            res.append(node.val)
        helper(root)
        return res
## ITERATIVE SOLN ######################################
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = [root]
        visit = [False]
        res = []

        while stack:
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visit.append(True)
                    for child in reversed(cur.children):
                        stack.append(child)
                        visit.append(False)
        return res
########################################################