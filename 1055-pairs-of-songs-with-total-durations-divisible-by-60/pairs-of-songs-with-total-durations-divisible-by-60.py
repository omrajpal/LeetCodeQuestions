class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        remainders = {}
        pairs = 0
        for i in time:
            r = i % 60
            if r == 0:
                pairs += remainders.get(r, 0)
            else:
                pairs += remainders.get(60-r, 0)
            remainders[r] = remainders.get(r, 0) + 1
        return pairs
        