class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        return n - abs(n - 1 - time % (n * 2 - 2))
        