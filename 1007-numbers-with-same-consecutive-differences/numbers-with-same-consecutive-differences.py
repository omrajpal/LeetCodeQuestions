class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []

        def dfs(num, l):
            if l == n:
                res.append(num)
                return
            last = num % 10
            if k != 0:
                nextDigits = [last - k, last + k]
            else:
                nextDigits = [last]
            for nextD in nextDigits:
                if 0 <= nextD < 10:
                    dfs(num*10 + nextD, l + 1)
        
        for i in range(1, 10):
            dfs(i, 1)
        
        return res
        