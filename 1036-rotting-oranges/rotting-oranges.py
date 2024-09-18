class Solution(object):
    from collections import deque
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        rotten = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        
        ## bfs
        queue = collections.deque()
        for i, j in rotten:
            queue.append((i, j))
        time = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while queue and fresh > 0:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for x, y in directions:
                    dx, dy = i + x, j + y
                    if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] == 1:
                        grid[dx][dy] = 2
                        fresh -= 1
                        queue.append((dx, dy))
            time += 1
        if fresh <= 0:
            return time
        return -1

