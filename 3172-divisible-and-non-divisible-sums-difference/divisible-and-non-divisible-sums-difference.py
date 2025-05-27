class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        total = n * (n + 1) // 2
        count = n // m
        divisible = m * count * (count + 1) // 2
        return total - 2 * divisible
        
        