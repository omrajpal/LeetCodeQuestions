class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        largest = 0
        stack = [] ## [start, height]
        for ind in range(len(heights)):
            i = heights[ind]
            start = ind
            while stack and stack[-1][1] > i:
                s, h = stack.pop()
                largest = max(largest, (ind-s)*h)
                start = s
            stack.append([start, i])
        for s, h in stack:
            largest = max(largest, (len(heights)-s)*h)
        return largest

                
        