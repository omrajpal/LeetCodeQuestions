class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        currTime = 0
        currMax = 0
        maxId = -1
        for i, time in logs:
            if time - currTime > currMax or (time - currTime == currMax and i < maxId):
                currMax = time - currTime
                maxId = i
            currTime = time
        return maxId

        