class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        posDict = {}
        wordsCopy = []
        pos = 0
        for i in words:
            wordsCopy.append(i)
            posDict[i] = pos
            pos += 1
        words.sort()
        pos = 0
        prefDict = {}
        ret = [0]*len(words)
        while pos < len(words):
            cur = ""
            wordScore = 0
            for i in words[pos]:
                cur += i
                score = 1
                if cur in prefDict:
                    score = prefDict[cur]
                else:
                    for j in words[pos+1:]:
                        if j[0:len(cur)] == cur:
                            score += 1
                        else:
                            break
                if score > 1:
                    prefDict[cur] = score
                wordScore += score
            ret[posDict[words[pos]]] = wordScore
            pos += 1
        return ret
print(Solution().sumPrefixScores(["abc","ab","bc","b"]))