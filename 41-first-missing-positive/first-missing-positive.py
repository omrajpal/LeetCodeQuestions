class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [n for n in nums if n > 0]
        
        for n in nums:
            if abs(n) <= len(nums) and nums[abs(n)-1] > 0:
                nums[abs(n)-1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
                
        return len(nums) + 1