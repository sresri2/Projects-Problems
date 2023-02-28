class Solution(object):
    def findDistanceBetweenNodes(self,node1,node2,connects):
        count = 0
        distancesFromNode1 = {}
        distancesFromNode1[node1] = 0
        visited = set()
        while node1 != -1:
            if node1 in visited:
                break
            visited.add(node1)
            node1 = connects[node1]
            if node1 == -1 or node1 in visited:
                break
            count += 1
            distancesFromNode1[node1] = count

        count = 0
        distancesFromNode2 = {}
        distancesFromNode2[node2] = 0
        visited2 = set()
        while node2!= -1:
            if node2 in visited2:
                break
            visited2.add(node2)
            node2 = connects[node2]
            if node2 == -1 or node2 in visited2:
                break
            count += 1
            distancesFromNode2[node2] = count
        
        return distancesFromNode1, distancesFromNode2
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        connects = {}
        pos = 0
        for i in edges:
            connects[pos] = i
            pos +=1 
            
        distFromNode1,distFromNode2 = self.findDistanceBetweenNodes(node1,node2,connects)
        poss = {}
        for i in list(distFromNode1.keys()):
            if i in distFromNode2:
                check = max(distFromNode1[i],distFromNode2[i])
                if check in poss:
                    if poss[check] > i:
                        poss[check] = i
                else:
                    poss[check] = i
        if len(poss) == 0:
            return -1
        return poss[min(list(poss.keys()))]
print(Solution().closestMeetingNode([5,3,1,0,2,4,5],3,2))