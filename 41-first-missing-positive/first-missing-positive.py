class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [n for n in nums if n > 0]
        nums = set(nums)

        target = 1
        while target in nums:
            target += 1
        
        return target