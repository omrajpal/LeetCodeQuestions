class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## go through the string, adding to a stack if open parenthesis, popping if closed
        stack = []
        to_remove = set()

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        # Add remaining unmatched '(' indices to remove set
        to_remove.update(stack)

        # Build result string skipping indices in to_remove
        return ''.join(c for i, c in enumerate(s) if i not in to_remove)