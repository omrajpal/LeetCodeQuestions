class Solution(object):
    import math
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans = []
        temp = ""
        tempArr = []
        sumWords = 0
        numWords = 0
        for word in words:
            if sumWords + len(word) + numWords > maxWidth:
                spaces = maxWidth - sumWords
                for i in range(len(tempArr) - 1):
                    temp += tempArr[i]
                    temp += " " * int(math.ceil(float(spaces)/(numWords - 1)))
                    spaces -= int(math.ceil(float(spaces)/(numWords - 1)))
                    numWords -= 1
                temp += tempArr[-1]
                if spaces > 0:
                    temp += " " * spaces
                ans.append(temp)
                tempArr = []
                sumWords = 0
                numWords = 0
                temp = ""

            tempArr.append(word)
            sumWords += len(word)
            numWords += 1
        spaces = maxWidth - sumWords
        for i in range(len(tempArr) - 1):
            temp += tempArr[i]
            temp += " "
            spaces -= 1
        temp += tempArr[-1]
        if spaces > 0:
            temp += " " * spaces
        ans.append(temp)
        return ans