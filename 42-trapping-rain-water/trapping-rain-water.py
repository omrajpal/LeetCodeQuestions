class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = len(height) - 1
        left = 0
        rm = height[right]
        lm = height[left]
        water = 0

        while left < right:
            if rm < lm:
                right -= 1
                rm = max(height[right], rm)
                water += rm - height[right]
            else:
                left += 1
                lm = max(height[left], lm)
                water += lm - height[left]   
        
        return water