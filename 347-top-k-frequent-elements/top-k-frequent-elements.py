class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res
