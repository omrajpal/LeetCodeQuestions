class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ans = []
        start, end = 0, 0 
        last = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            end = max(end, last[c]) ## gets last occurence (min length of partition)

            if i == end:
                ans.append(end - start + 1)
                start = end + 1
                end += 1
        
        return ans
        