class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        runningSum = 0
        hashmap = {0: 1}
        for num in nums:
            runningSum += num
            if runningSum - k in hashmap:
                count += hashmap[runningSum - k]
            hashmap[runningSum] = hashmap.get(runningSum, 0) + 1
        
        return count

        