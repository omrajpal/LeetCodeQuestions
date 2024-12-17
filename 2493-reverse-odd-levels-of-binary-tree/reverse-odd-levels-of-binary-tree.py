# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        def reverseLevels(left, right, level):
            if not left or not right:
                return None
            if level % 2 == 1:
                left.val, right.val = right.val, left.val
            reverseLevels(left.left, right.right, level + 1)
            reverseLevels(right.left, left.right, level + 1)
        reverseLevels(root.left, root.right, 1)
        return root

        