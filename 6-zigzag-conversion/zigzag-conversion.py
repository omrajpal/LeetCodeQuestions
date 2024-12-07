class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = ["" for _ in range(numRows)]
        i = 0
        direction = True
        for c in s:
            rows[i] += c
            if i == numRows - 1:
                direction = False
            elif i == 0:
                direction = True
            if direction:
                i += 1
            else:
                i -= 1

        sol = ""
        for r in rows:
            sol += r
        
        return sol


        