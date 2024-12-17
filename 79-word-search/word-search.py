class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        visited = set()
        def dfs(i, row, col):
            if i == len(word):
                return True
            visited.add((row, col))
            for dx, dy in directions:
                x, y = row + dx, col + dy
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in visited and board[x][y] == word[i]:
                    if dfs(i + 1, x, y):
                        return True
            visited.remove((row, col))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(1, i, j):
                        return True
        return False

        