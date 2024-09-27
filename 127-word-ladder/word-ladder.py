class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        setWords = set(wordList)
        if endWord not in setWords:
            return 0
        queue = collections.deque()
        queue.append(beginWord)
        distance = 1

        while queue:
            size = len(queue)
            distance += 1

            for _ in range(size):
                word = queue.popleft()
                for j in range(len(word)):
                    for i in range(26):
                        char = chr(ord('a') + i)
                        if char == word[j]:
                            continue
                        newWord = word[:j] + char + word[j+1:]
                        if newWord == endWord:
                            return distance
                        if newWord in setWords:
                            print(newWord)
                            print(distance)
                            setWords.remove(newWord)
                            queue.append(newWord)
        return 0
        