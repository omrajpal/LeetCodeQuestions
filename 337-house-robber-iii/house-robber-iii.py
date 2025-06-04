# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def helper(node):
            if not node:
                return 0, 0
            l1, l2 = helper(node.left)
            r1, r2 = helper(node.right)
            rob = node.val + l2 + r2
            notRob = max(l1, l2) + max(r1, r2)
            return rob, notRob
        
        return max(helper(root))

        