class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        runningSum = 0
        ans = float("inf")
        start = 0
        end = 0
        for num in nums:
            runningSum += num
            while runningSum >= target:
                ans = min(ans, end - start + 1)
                runningSum -= nums[start]
                start += 1
            end += 1
        
        return 0 if ans == float("inf") else ans

        