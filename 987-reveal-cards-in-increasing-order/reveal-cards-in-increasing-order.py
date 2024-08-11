class Solution(object):
    import math
    from collections import deque
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort(reverse=True)
        n = len(deck)
        deck = deque(deck)
        ans = deque()
        while len(ans) < n:
            ans.appendleft(deck.popleft())
            ans.appendleft(ans.pop())
        ans.append(ans.popleft())
        print(ans)
        return ans