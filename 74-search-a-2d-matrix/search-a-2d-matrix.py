class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
    
        # Matrix dimensions
        rows, cols = len(matrix), len(matrix[0])
        
        # Binary search on the 2D matrix treated as a 1D array
        left, right = 0, rows * cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Convert the 1D mid index back to 2D row and column
            mid_value = matrix[mid // cols][mid % cols]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
            