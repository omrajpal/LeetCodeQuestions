"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        graph = {}
        graph[node] = Node(node.val)
        stack = [node]
        while stack:
            curr = stack.pop()
            for neighbor in curr.neighbors:
                if neighbor not in graph:
                    graph[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                
                graph[curr].neighbors.append(graph[neighbor])
        
        return graph[node]