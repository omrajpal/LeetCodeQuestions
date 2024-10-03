class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        def helper(idx, sol):
            if len(sol) == len(digits):
                res.append(sol[:])
                return
            
            for c in mapping[digits[idx]]:
                helper(idx + 1, sol + c)
        
        helper(0, "")

        return res
        