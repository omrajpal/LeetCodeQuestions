class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        if not timePoints:
            return
        minutes = []
        for time in timePoints:
            hrs = int(time[0:2])
            mins = int(time[3:5])
            temp = hrs*60 + mins
            minutes.append(temp)
        minutes.sort()
        print(minutes)

        minD = float('inf')
        last = minutes[0]
        for i in range(1, len(minutes)):
            m = minutes[i]
            if m - last >= 720:
                minD = min(minD, abs(m - last - 1440))
            else:
                minD = min(minD, m - last)
            last = m
            print(minD)
        m = minutes[0]
        diff = abs(m - last)
        if diff >= 720:
            minD = min(minD, abs(diff - 1440))
        else:
            minD = min(minD, diff)

        return minD

        