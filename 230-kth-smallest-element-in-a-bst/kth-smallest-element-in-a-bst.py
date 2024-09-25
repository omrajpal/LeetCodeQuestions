# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.ans = None
        self.k = k
        def helper(node):
            if not node:
                return
            helper(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            rightNodes = helper(node.right)

        helper(root)
        return self.ans