class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        ## heap shows the tasks with increasing processing times that are currently available
        ## while loop 

        tasks = sorted([(enqueue, process, i) for i, (enqueue, process) in enumerate(tasks)])
        res = []
        time = tasks[0][0]
        heap = []
        i = 0
        while len(res) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if heap:
                processing_time, index = heapq.heappop(heap)
                time += processing_time
                res.append(index)
            elif i < len(tasks):
                time = tasks[i][0]
        return res

        