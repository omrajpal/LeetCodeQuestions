class MedianFinder(object):

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.maxHeap, -num) ## stores max of high numbers
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap)) ## stores min of high numbers
        while len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -1*self.maxHeap[0]) / 2.0
        return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()