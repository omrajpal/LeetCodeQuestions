class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def helper(arr, used):
            if len(arr) == len(nums):
                ans.append(arr)
                return
            
            for i in nums:
                if i not in used:
                    used.add(i)
                    helper(arr + [i], set(used))
                    used.remove(i)
        helper([], set())
        return ans
        