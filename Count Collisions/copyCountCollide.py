class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """

        count = 0
        pos = 0
        dupe = "L"
        for car in directions:
            if car == "R":
                if pos != len(directions)-1:
                    if directions[pos+1] == "S":
                        count += 1
                        dupe +="S"
                    else:
                        dupe += "R"

            if car == "L":
                if pos != 0:
                    if directions[pos-1]=="R":
                        count += 2
                        dupe = dupe[0:len(dupe)-1]
                        dupe += "S"
                    elif dupe[-1]=="S":
                        count += 1
                        dupe += "S"
                    else:
                        dupe+="L"
            else:
                dupe += "S"
            pos += 1
        
        print(dupe)
        pos = len(dupe)-1
        for car in dupe[::-1]:
            if car == "R":
                if pos != len(dupe)-1:
                    if dupe[pos+1] == "S":
                        count += 1
                        dupe = dupe[0:pos]+"S"+dupe[pos+1:]
            if car == "L":
                if pos != 0:
                    if dupe[pos-1]=="S":
                        count += 1
            pos -= 1
        return count

print(Solution().countCollisions("LSSSLLSSSSLRRSLLLSLSLRRLLLLLRSSRSRRSLLLSSS"))