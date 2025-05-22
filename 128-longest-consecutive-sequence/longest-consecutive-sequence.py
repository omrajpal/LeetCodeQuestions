class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        ans = 0

        for num in numSet:
            if num - 1 not in numSet:
                count = 1
                while num + 1 in numSet:
                    count += 1
                    num += 1
                ans = max(ans, count)
        return ans
        