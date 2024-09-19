class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        higher = max(piles)
        lower = 1
        while lower < higher:
            mid = (lower + higher) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / float(mid))\
            
            if hours > h:
                lower = mid + 1
            else:
                higher = mid
        return lower
            

            

                
        