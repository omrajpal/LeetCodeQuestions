class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        maxHeap = [[-cnt, c] for c, cnt in count.items()]
        heapq.heapify(maxHeap)
        if -1 * maxHeap[0][0] > (len(s) + 1) // 2:
            return ""
        prevCnt, prev = 0, ''

        res = ""
        while maxHeap:
            cnt, c = heapq.heappop(maxHeap)
            res += c
            cnt += 1

            if prevCnt < 0:
                heapq.heappush(maxHeap, [prevCnt, prev])
            prevCnt, prev = 0, ''
            if cnt < 0:
                prevCnt, prev = cnt, c
        
        return res