class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        lossOne = set()
        lossGreaterOne = set()
        for i in matches:
            if i[1] not in lossOne and i[1] not in lossGreaterOne:
                lossOne.add(i[1])
            elif i[1] in lossOne:
                lossOne.remove(i[1])
                lossGreaterOne.add(i[1])

        done = set()
        ret= [[],[]]
        for i in matches:
            if i[0] not in done:
                if i[0] not in lossOne and i[0] not in lossGreaterOne:
                    ret[0].append(i[0])
                elif i[0] in lossOne:
                    ret[1].append(i[0])
                done.add(i[0])
            if i[1] not in done:
                if i[1] not in lossOne and i[1] not in lossGreaterOne:
                    ret[0].append(i[1])
                elif i[1] in lossOne:
                    ret[1].append(i[1])

                done.add(i[1])

        ret[0].sort()
        ret[1].sort()

        return ret

print(Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))