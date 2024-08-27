class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        ans = 0
        for num in nums:
            if num == ans:
                count += 1
            else:
                count -= 1
                if count == 0:
                    ans = num
                    count = 1
        
        return ans