class Solution(object):
    def getCosts(self,findCosts,pos,days,cost,costs):

        if pos >= len(days)-1:
            return cost

        day = days[pos + 1]
        cost += costs[0] + self.getCosts(findCosts,pos+1,days,cost,costs)
        givePos = 6
        if day + 6 in days:
            pos += 6
            givePos = pos
        else:
            found = False
            search = 5
            while not found:
                searchNum = day + search
                if searchNum in days:
                    found = True
                    givePos = day - search
                else:
                    search -= 1

        cost += costs[1] + self.getCosts(findCosts,givePos,days,cost,costs)


        givePos = 29
        if day + 29 in days:
            pos += 29
            givePos = pos
        else:
            found = False
            search = 29
            while not found:
                searchNum = day + search
                if searchNum in days:
                    found = True
                    givePos = day = search
                else:
                    search -= 1


        cost += costs[2] + self.getCosts(findCosts,givePos,days,cost,costs)
    def mincostTickets(self, days, costs):
        findCosts = []
        pos = 0
        
        day = days[pos]

        curCost = 0
        curCost = costs[0] + self.getCosts(findCosts,pos,days,curCost,costs)

        findCosts.append(curCost)

        givePos = 6
        if day + 6 in days:
            pos += 6
            givePos = pos
        else:
            found = False
            search = 5
            while not found:
                searchNum = day + search
                if searchNum in days:
                    found = True
                    givePos = day = search
                else:
                    search -= 1

        curCost = costs[1] + self.getCosts(findCosts,givePos,days,curCost,costs)

        findCosts.append(curCost)

        givePos = 29
        if day + 29 in days:
            pos += 29
            givePos = pos
        else:
            found = False
            search = 29
            while not found:
                searchNum = day + search
                if searchNum in days:
                    found = True
                    givePos = day = search
                else:
                    search -= 1


        curCost = costs[2] + self.getCosts(findCosts,givePos,days,curCost,costs)

        findCosts.append(curCost)


        return min(findCosts)
        
        
print(Solution().mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31],[2,7,15]))
            