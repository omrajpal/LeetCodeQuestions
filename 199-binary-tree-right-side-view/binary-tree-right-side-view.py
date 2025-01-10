# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        trav = [[]]
        res = []
        dq = deque([root])
        def bfs():
            i = 0
            while dq:
                if len(trav) <= i:
                    trav.append([])
                for _ in range(len(dq)):
                    curr = dq.popleft()
                    trav[i].append(curr.val)
                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right) 
                res.append(trav[i][-1])
                i += 1
        bfs()
        return res
                
                
            

        