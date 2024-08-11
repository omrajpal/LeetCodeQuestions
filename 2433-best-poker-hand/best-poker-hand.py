class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        hashmap = {}
        flush = True
        pair = False
        three = False
        past = suits[-1]
        for rank, suit in zip(ranks, suits):
            if suit != past:
                flush = False
            hashmap[rank] = 1 + hashmap.get(rank, 0)
            if hashmap[rank] == 2:
                pair = True
            elif hashmap[rank] == 3:
                three = True
        
        return "Flush" if flush else "Three of a Kind" if three else "Pair" if pair else "High Card"
            
        