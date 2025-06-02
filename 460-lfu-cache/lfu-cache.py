class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None

    def pop(self):
        if self.tail is None:
            return None
        old_tail = self.tail
        self.remove(old_tail)
        return old_tail

    def is_empty(self):
        return self.head is None

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.keyMap = {}       # key -> node
        self.freqMap = {}      # freq -> Deque
        self.minFreq = 0

    def get(self, key):
        if key not in self.keyMap:
            return -1

        node = self.keyMap[key]
        self._update_freq(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = value
            self._update_freq(node)
        else:
            if self.size == self.capacity:
                # Evict least frequently used and least recently used
                to_remove = self.freqMap[self.minFreq].pop()
                del self.keyMap[to_remove.key]
                self.size -= 1

            new_node = Node(key, value)
            self.keyMap[key] = new_node
            if 1 not in self.freqMap:
                self.freqMap[1] = Deque()
            self.freqMap[1].add(new_node)
            self.minFreq = 1
            self.size += 1

    def _update_freq(self, node):
        freq = node.freq
        self.freqMap[freq].remove(node)
        if self.freqMap[freq].is_empty():
            del self.freqMap[freq]
            if self.minFreq == freq:
                self.minFreq += 1

        node.freq += 1
        if node.freq not in self.freqMap:
            self.freqMap[node.freq] = Deque()
        self.freqMap[node.freq].add(node)