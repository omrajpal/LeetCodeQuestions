class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        res = [[]]
        def helper(curr, used):
            for i in nums:
                if i not in used:
                    res.append(curr + [i])
                    used.add(i)
                    helper(curr + [i], set(used))
        helper([], set())
        return res
        