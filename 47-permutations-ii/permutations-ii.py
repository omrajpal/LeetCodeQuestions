class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        def helper(arr, uses):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return
            prev = -11
            for i in nums:
                if i == prev:
                    prev = i
                    continue
                if uses[i] > 0:
                    uses[i] -= 1
                    arr.append(i)
                    helper(arr, uses)
                    arr.pop()
                    uses[i] += 1
                prev = i
            
        helper([], Counter(nums))
        return ans

        