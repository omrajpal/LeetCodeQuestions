class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        values = [(value, key) for key, value in count.items()]
        values.sort(reverse=True)
        return [key for value, key in values[:k]]