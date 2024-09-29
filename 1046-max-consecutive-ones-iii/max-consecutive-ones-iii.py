class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, 0
        count = 0
        maxOnes = 0
        for i in nums:
            if i == 0:
                count += 1
            right += 1
            if count > k:
                while nums[left] != 0:
                    left += 1
                left += 1
                count -= 1
            maxOnes = max(maxOnes, right - left)
        return maxOnes

        