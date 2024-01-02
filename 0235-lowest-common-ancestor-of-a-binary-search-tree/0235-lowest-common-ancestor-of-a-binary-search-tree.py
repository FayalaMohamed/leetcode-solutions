# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        it = root
        while it:
            if p.val < it.val and q.val < it.val:
                it = it.left
            elif p.val > it.val and q.val > it.val:
                it = it.right
            else:
                return it