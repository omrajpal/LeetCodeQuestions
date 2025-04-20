from collections import deque
class FrontMiddleBackQueue(object):

    def __init__(self):
        self.front = deque()
        self.second = deque()

    
    def rebalance(self):
        while len(self.front) > len(self.second):
            self.second.appendleft(self.front.pop())
        while len(self.front) + 1 < len(self.second):
            self.front.append(self.second.popleft())

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.front.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.second.appendleft(val)
        self.rebalance()          
        

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.second.append(val)
        self.rebalance()
        

    def popFront(self):
        """
        :rtype: int
        """
        if len(self.front) > 0:
            ans = self.front.popleft()
        elif len(self.second) > 0:
            ans = self.second.popleft()
        else: 
            return -1
        self.rebalance()
        return ans
        

    def popMiddle(self):
        """
        :rtype: int
        """
        if not self.front and not self.second:
            return -1
        if len(self.front) == len(self.second):
            ans = self.front.pop()
        else:
            ans = self.second.popleft()
        self.rebalance()
        return ans
        

    def popBack(self):
        """
        :rtype: int
        """
        if len(self.second) > 0:
            ans = self.second.pop()
        else: 
            return -1
        self.rebalance()
        return ans
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()