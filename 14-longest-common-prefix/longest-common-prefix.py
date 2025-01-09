class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or not strs[0]:
            return ""
        l = 0
        done = False
        maxL = min([len(s) for s in strs])
        while True:
            if l >= maxL: 
                break
            c = strs[0][l]
            for s in strs:
                if s[l] != c:
                    done = True
                    break
            if done:
                break
            l += 1
        return strs[0][:l]


            