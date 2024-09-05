class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxVal = 0
        while left < right:
            width = right - left
            maxVal = max(maxVal, width*min(height[left], height[right]))
            if height[left] - height[right] < 0:
                left += 1
            else:
                right -= 1
        return maxVal

        