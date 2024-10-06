class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def helper(isLeft):
            l, r = 0, len(nums) - 1
            idx = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    idx = mid
                    if isLeft:
                        r = mid - 1
                    else:
                        l = mid + 1
            return idx
        
        left = helper(True)
        right = helper(False)
        return [left, right]
        