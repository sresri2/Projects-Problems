class Solution(object):
    def validatePosition(self, val, listOfDep, listOfCourses):
        pos = 0
        maxDepPos = 0
        coursePos = 0
        for course in listOfCourses:
            if course == val:
                coursePos = pos
            if course in listOfDep:
                maxDepPos = pos
            pos+=1
        if maxDepPos > coursePos:
            return False
        else:
            return True

    def addDependencies(self, dictionary, val, finalList, depGraph):
        if (val not in dictionary):
            if (val not in finalList):
                finalList.append(val)
            return True
        if val in depGraph:
            return True
        else:
            depGraph.append(val)
        for dep in dictionary[val]:
            if not self.addDependencies(dictionary,dep, finalList, depGraph):
                return False

        if val not in finalList:
            finalList.append(val)
        else:
            return self.validatePosition(val, dictionary[val], finalList)
        return True

    def getOrder(self,dictionary,list):
        finalList = []
        list.sort()
        for val in list:
            if not val in finalList:
                depGraph = []
                if not self.addDependencies(dictionary, val, finalList, depGraph):
                    return [-1]
            
        return finalList

    def findOrder(self, numCourses, prerequisites):
        if prerequisites == []:
            finalList = []
            for i in range(0,numCourses):
                finalList.append(i)
            finalList.sort(reverse = True)
            return finalList
        dict = {}
        list = []
        for item in prerequisites:
            if item[0] not in dict:
                dict[item[0]] = [item[1]]
                list.append(item[0])
            else:
                dict[item[0]].append(item[1])
        finalList = Solution().getOrder(dict,list)
        if finalList[0] == -1:
            return []
        if len(finalList) == numCourses:
            return finalList
        for i in range(0,numCourses):
            if i not in finalList:
                finalList.append(i)
        
        return finalList



print(Solution().findOrder(2,[[1,0],[0,1]]))