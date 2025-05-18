class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.sums = []
            return

        m, n = len(matrix), len(matrix[0])
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                self.sums[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.sums[i][j + 1]
                    + self.sums[i + 1][j]
                    - self.sums[i][j]
                )

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (
            self.sums[row2 + 1][col2 + 1]
            - self.sums[row1][col2 + 1]
            - self.sums[row2 + 1][col1]
            + self.sums[row1][col1]
        )