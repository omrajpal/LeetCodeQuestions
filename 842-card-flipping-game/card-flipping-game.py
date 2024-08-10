class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        doubles = set()
        for i, j in zip(fronts, backs):
            if i == j:
                doubles.add(i)
        res = (set(fronts + backs)) - doubles
        return min(res) if res else 0
        
        