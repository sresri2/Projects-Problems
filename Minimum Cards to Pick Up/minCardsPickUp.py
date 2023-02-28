class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        noMatchYet= {}
        matchFound = {}
        pos = 0
        for i in cards:
            if i not in matchFound and i not in noMatchYet:
                noMatchYet[i]=pos
            elif i in noMatchYet:
                if i not in matchFound:
                    matchFound[i] = pos-(noMatchYet[i])+1
                else:
                    if pos-(noMatchYet[i])+1 < matchFound[i]:
                        matchFound[i] = pos-(noMatchYet[i])+1
                noMatchYet[i] = pos
            pos += 1
        if len(matchFound)>0:
            return min(list(matchFound.values()))
        else:
            return -1

print(Solution().minimumCardPickup([3,4,2,3,4,7]))