class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]] n x m
        :rtype: int
        """
        count = 0
        n = len(grid)
        m = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            print(x)
            print(y)
            grid[x][y] = "0"
            for x1, y1 in directions:
                if 0 <= x+x1 < n and 0 <= y+y1 < m and grid[x+x1][y+y1] == "1":
                    dfs(x+x1, y+y1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count
