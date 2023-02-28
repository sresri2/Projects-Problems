class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        """
        :type creators: List[str]
        :type ids: List[str]
        :type views: List[int]
        :rtype: List[List[str]]
        """
        '''
        popularity Dict
        creatorIdsDict
        '''
        popDict = {}
        vals = {}
        for i in range(0,len(creators)):
            if creators[i] not in popDict:
                popDict[creators[i]] = views[i]
                vals[creators[i]] = {ids[i]:views[i]}
            else:
                popDict[creators[i]] += views[i]
                if ids[i] in vals[creators[i]]:
                    if views[i] > vals[creators[i][ids[i]]]:
                        vals[creators[i]][ids[i]] = views[i]
                else:
                    vals[creators[i]][ids[i]] = views[i]
        
        maxPop = max(list(popDict.values()))
        mostPops = []
        for i in list(popDict.keys()):
            if popDict[i] == maxPop:
                mostPops.append(i)
        
        res = []
        for i in mostPops:
            maxViews = max(list(vals[i].values()))
            mostVids = []
            for j in list(vals[i].keys()):
                if vals[i][j]==maxViews:
                    mostVids.append(j)
            mostVids.sort()
            res.append([i,mostVids[0]])
        sorted(res, key=lambda x: x[0])
        return res

print(Solution().mostPopularCreator(["alice","bob","alice","chris"],["one","two","three","four"],[5,10,5,4]))