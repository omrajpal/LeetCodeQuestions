class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        answer = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp > stack[-1][1]:
                index, prev = stack.pop()
                answer[index] = i - index
            stack.append([i, temp])
        return answer