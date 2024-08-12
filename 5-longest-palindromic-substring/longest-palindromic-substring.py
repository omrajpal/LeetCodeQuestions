class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        longest = 1
        ans = s[0]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j<= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > longest:
                        longest = i-j+1
                        ans = s[j:i+1]
        return ans

        