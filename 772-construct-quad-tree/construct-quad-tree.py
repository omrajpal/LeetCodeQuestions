"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def helper(i, j, length):
            # Check if all values in the subgrid are the same
            def allSame(i, j, length):
                val = grid[i][j]
                for y in range(i, i + length):
                    for x in range(j, j + length):
                        if grid[y][x] != val:
                            return False
                return True

            # Base case: all values in current subgrid are same
            if allSame(i, j, length):
                return Node(grid[i][j] == 1, True)

            # Recursive case: split into 4 quadrants
            half = length // 2
            return Node(
                val=False,
                isLeaf=False,
                topLeft=helper(i, j, half),
                topRight=helper(i, j + half, half),
                bottomLeft=helper(i + half, j, half),
                bottomRight=helper(i + half, j + half, half)
            )
        
        return helper(0, 0, len(grid))