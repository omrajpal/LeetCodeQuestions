# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.i = 0
        inOrderMap = {element: i for i, element in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return 
            
            root = TreeNode(preorder[self.i])
            self.i += 1
            
            root.left = helper(left, inOrderMap[root.val] - 1)
            root.right = helper(inOrderMap[root.val] + 1, right)

            return root
        return helper(0, len(preorder) - 1)