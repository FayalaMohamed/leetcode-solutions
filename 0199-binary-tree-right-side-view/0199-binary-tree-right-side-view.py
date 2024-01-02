# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        res = []
        if root :
            res.append(root.val)
        
        it = root
        while it :
            if it.right:
                it = it.right
            else: 
                it = it.left
            if it:
                res.append(it.val)
        return res
        """

        q = deque()
        if root :
            q.append(root)
        
        res = []
        while q :
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level[-1])
        return res



