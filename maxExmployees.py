class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        counts = {}
        posDict = {}
        pos = 0
        marked = []
        markedDict = {}
        for i in favorite:
            if i in counts:
                favorite[i]+=1
                if i not in markedDict:

            else:
                favorite[i]=1
            
            pos += 1
        
                    
        
            
