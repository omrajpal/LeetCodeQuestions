class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## go through the string, adding to a stack if open parenthesis, popping if closed
        stack = []
        opens = []
        ans = [""] * len(s)
        curr = 0
        for i in range(len(s)):
            c = s[i]
            if c == ')':
                if len(stack) == 0:
                    continue
                stack.pop()
            elif c == '(':
                stack.append('(')
                opens.append(curr)
            ans[curr] = c
            curr += 1

        if len(stack) > 0:
            for i in range(len(opens) - 1, len(opens) - len(stack) - 1, -1): ## index of last open parenthesis, until len(stack) is resolved
                temp = opens[i]
                ans[temp] = ""
        
        return ''.join(ans)
