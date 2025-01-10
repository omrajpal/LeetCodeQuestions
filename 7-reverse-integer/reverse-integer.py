class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            neg = True
            x *= -1
        rev = 0
        while x > 0:
            rev = rev*10 + x%10
            x /= 10

        if rev > 2 ** 31 - 1 or rev < -2 ** 31:
            return 0
        
        return rev*-1 if neg else rev

        