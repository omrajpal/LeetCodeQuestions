class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## maintain a count
        count = 0
        ## left and right variable
        left = right = 0
        ## while right isnt at end of array
        while right < len(nums) - 1:
        ## set a furthest/temp variable which keeps track of how far we can go
            furthest = 0
        ## go through the left - right range, find the furthest we can go
            for i in range(left, right + 1):
                furthest = max(furthest, i + nums[i])
        ## update the pointers- left goes to right + 1, right goes to furthest
            count += 1
            left = right + 1
            right = furthest
        ## update count
        return count
        