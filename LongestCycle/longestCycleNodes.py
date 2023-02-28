class Solution(object):
    def findCycle(self,node1,connects):
        count = 0
        visited = set()
        distanceFromSt = {}
        distanceFromSt[node1] = 0
        while node1 != -1:
            count += 1
            if node1 in visited:
                return count - distanceFromSt[node1]-1
            visited.add(node1)
            node1 = connects[node1]
            if node1 not in visited:
                distanceFromSt[node1] = count
           
            if node1 == -1:
                return -1
  
        
        return -1
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        connects = {}
        pos = 0
        for i in edges:
            connects[pos] = i
            pos +=1 
        
        cur = -1
        for i in list(connects.keys()):
            check = self.findCycle(i,connects) 
            if check !=-1:
                if check > cur:
                    cur = check
        return cur

print(Solution().longestCycle([3,3,4,2,3]))