class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        letterDict = {}
        for i in S:
            if i not in letterDict:
                letterDict[i] = 1
            else:
                letterDict[i] += 1

        lettersFound = {}
        part = []
        cur = ""
        for i in S:
            cur += i
            if i not in lettersFound:
                lettersFound[i] = 1
            else:
                lettersFound[i] += 1

            if lettersFound[i] == letterDict[i]:
                del(lettersFound[i])

            if len(lettersFound) == 0:
                part.append(len(cur))
                cur = ""


        return part


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))