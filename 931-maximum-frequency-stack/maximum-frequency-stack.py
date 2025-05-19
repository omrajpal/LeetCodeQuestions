class FreqStack(object):
    # freq holds value -> freq, vals holds freq -> values
    def __init__(self):
        self.freq = {}
        self.vals = collections.defaultdict(list)
        self.maxf = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        freq, vals = self.freq, self.vals
        freq[val] = freq.get(val, 0) + 1
        vals[freq[val]].append(val)
        self.maxf = max(self.maxf, freq[val])
        

    def pop(self):
        """
        :rtype: int
        """
        while self.maxf > 0 and not self.vals[self.maxf]: 
            self.maxf -= 1
        freq, vals, maxf = self.freq, self.vals, self.maxf
        x = vals[maxf].pop()
        if not vals[maxf]:
            maxf -= 1
        freq[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()