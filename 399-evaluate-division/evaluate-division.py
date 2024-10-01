import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = value
            graph[b][a] = 1.0 / value

        results = []
        for query in queries:
            start = query[0]
            end = query[1]
            if start not in graph or end not in graph:
                results.append(-1)
                continue
            visited = set()
            queue = collections.deque([(start, 1.0)])
            results.append(-1)
            while queue:
                node, multiplier = queue.popleft()
                if node == end:
                    results[-1] = multiplier
                    break
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, multiplier * graph[node][neighbor]))
        return results