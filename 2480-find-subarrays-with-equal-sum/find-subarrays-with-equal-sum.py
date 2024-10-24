class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        all_sums = set()
        for i in range(0, len(nums) - 1):
            if nums[i] + nums[i + 1] in all_sums:
                return True
            else:
                all_sums.add(nums[i] + nums[i + 1])
    
        return False

        