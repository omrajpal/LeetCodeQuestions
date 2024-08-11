class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        temp = groupSize - 1
        bins = len(hand) // groupSize
        hand.sort()
        hashmap = {i: [] for i in range(bins)}

        for card in hand:
            placed = False
            for i in range(bins):
                temp = hashmap[i]
                if len(temp) >= groupSize:
                    continue
                if temp == [] or temp[-1] == card - 1:
                    hashmap[i].append(card)
                    placed = True
                    break
            if not placed:
                return False
        return True


        