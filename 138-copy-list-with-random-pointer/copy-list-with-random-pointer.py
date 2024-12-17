"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        node_map = {}
        current = head
        
        # First pass: Create a copy of each node and store it in the map
        while current:
            node_map[current] = Node(current.val)
            current = current.next
        
        current = head
        
        # Second pass: Connect the copied nodes' next and random pointers
        while current:
            copy_node = node_map[current]
            copy_node.next = node_map.get(current.next)
            copy_node.random = node_map.get(current.random)
            current = current.next
        
        return node_map[head]
