class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float('-inf')
        curr = 0
        for num in nums:
            curr += num
            ans = max(ans, curr)
            if curr < 1:
                curr = 0

        return ans
        