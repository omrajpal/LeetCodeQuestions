class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        n = len(nums)
        _sum = sum(nums)

        i, j = 1, max(nums)
        minDivisor = max(nums)

        while i <= j:
            mid = (i + j) // 2

            currSum = 0

            for num in nums:
                currSum += (num + mid - 1) // mid

            if currSum <= threshold:
                minDivisor = min(minDivisor, mid)
                j = mid - 1
            else:
                i = mid + 1

        return minDivisor