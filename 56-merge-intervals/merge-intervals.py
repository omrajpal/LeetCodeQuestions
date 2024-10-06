class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        res = []
        curr = intervals[0]
        for start, end in intervals[1:]:
            if start <= curr[1]:
                curr[1] = max(end, curr[1])
            else:
                res.append(curr)
                curr = [start, end]
        res.append(curr)
        return res
        
