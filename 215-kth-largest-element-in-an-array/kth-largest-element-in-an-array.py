class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        x = min(nums)
        arr = [0] * (max(nums) - x + 1)
        
        for num in nums:
            temp = num - x
            arr[temp] += 1
        
        y = len(arr) - 1
        while True:
            k -= arr[y]
            if k <= 0:
                return x + y
            y -= 1
