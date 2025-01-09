class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = set()
        for i in nums:
            if i in n:
                n.remove(i)
            else:
                n.add(i)
        return n.pop()
        