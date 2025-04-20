from array import array

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = array('i', [0] * k)  # 'i' = signed int
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if value is None:
            return False
        if self.size >= self.capacity:
            return False
        self.queue[self.rear] = value
        self.rear += 1
        if self.rear == self.capacity:
            self.rear = 0
        self.size += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.size <= 0:
            return False
        ans = self.queue[self.front]
        self.size -= 1
        self.front += 1
        if self.front == self.capacity:
            self.front = 0
        return True

        

    def Front(self):
        """
        :rtype: int
        """
        if self.size <= 0:
            return -1
        return self.queue[self.front]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.size <= 0:
            return -1
        return self.queue[(self.rear - 1) % self.capacity]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()