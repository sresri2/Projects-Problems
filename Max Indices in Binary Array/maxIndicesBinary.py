class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftDict = {
            0:0,
            1:0
        }
        rightDict = {
            0:0,
            1:0
        }
        for i in nums:
            rightDict[i]+=1

        pos = 0
        indices = []
        indicesDict = {}
        maxIndice = None
        while pos < len(nums):
            indice = leftDict[0]+rightDict[1]
            indices.append(indice)
            if indice not in indicesDict:
                indicesDict[indice]=[pos]
            else:
                indicesDict[indice].append(pos)
            if maxIndice== None:
                maxIndice = indice
            elif indices[-1]>maxIndice:
                maxIndice=indice

            leftDict[nums[pos]]+=1
            rightDict[nums[pos]]-=1
            pos += 1
        indice = leftDict[0]+rightDict[1]
        indices.append(leftDict[0]+rightDict[1])
        if indice not in indicesDict:
            indicesDict[indice]=[pos]
        else:
            indicesDict[indice].append(pos)
        if indice>maxIndice:
            maxIndice=indice
        return indicesDict[maxIndice]

print(Solution().maxScoreIndices([0,0,1,0]))

        