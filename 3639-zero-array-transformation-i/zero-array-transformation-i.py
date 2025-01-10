class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        freq = [0] * len(nums)
        for l, r in queries:
            freq[l] += 1
            if r + 1 < len(nums):
                freq[r+1] -= 1
        
        curr = 0
        for num, f in zip(nums, freq):
            curr += f
            if num > curr:
                return False
        
        return True
        