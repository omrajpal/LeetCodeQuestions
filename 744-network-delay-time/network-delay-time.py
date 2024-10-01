import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            adj[u].append((v, w))
        heap = [(0, k)]
        maxVal = float('-inf')
        visited = set()
        while len(visited) != n and heap:
            dist, node = heapq.heappop(heap)
            maxVal = max(dist, maxVal)
            if node in visited:
                continue
            visited.add(node)
            for neigh, weight in adj[node]:
                if neigh not in visited:
                    heapq.heappush(heap, (dist + weight, neigh))
        return maxVal if len(visited) == n else -1


        