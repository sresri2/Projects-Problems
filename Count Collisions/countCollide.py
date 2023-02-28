class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """

        count = 0
        pos = 0
        for car in directions:
            if car == "R":
                if pos != len(directions)-1:
                    if directions[pos+1] == "S":
                        count += 1
                        directions = directions[0:pos]+"S"+directions[pos+1:]
            if car == "L":
                if pos != 0:
                    if directions[pos-1]=="R":
                        count += 2
                        directions = directions[0:pos-1]+"SS"+directions[pos+1:]
                    elif directions[pos-1]=="S":
                        count += 1
                        directions = directions[0:pos]+"S"+directions[pos+1:]
            pos += 1
            print(count)
        print(directions)
        pos = len(directions)-1
        for car in directions[::-1]:
            if car == "R":
                if pos != len(directions)-1:
                    if directions[pos+1] == "S":
                        count += 1
                        directions = directions[0:pos]+"S"+directions[pos+1:]
            if car == "L":
                if pos != 0:
                    if directions[pos-1]=="R":
                        count += 2
                        directions = directions[0:pos-1]+"SS"+directions[pos+1:]
                    elif directions[pos-1]=="S":
                        count += 1
                        directions = directions[0:pos]+"S"+directions[pos+1:]
            pos -= 1
        return count

print(Solution().countCollisions("LLRLRLLSLRLLSLSSSS"))
