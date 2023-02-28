class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        pos = 0
        numLefts =0
        numRights = 0
        while pos < len(start):
            if start[pos] == "L" and target[pos] == "L":
                if numRights > 0:
                    return False
            if start[pos] == "L" and target[pos] == "_":
                if numLefts == 0 or numRights >0:
                    return False
                numLefts-=1
            if start[pos] == "L" and target[pos] == "R":
                if numLefts == 0 or numRights == 0:
                    return False
                numLefts -= 1
                numRights -= 1
            if start[pos] == "_" and target[pos] == "L":
                numLefts += 1
            if start[pos] == "_" and target[pos] == "R":
                if numRights == 0:
                    return False
                numRights -=1
            if start[pos] == "R" and target[pos] == "L":
                return False
            if start[pos] == "R" and target[pos] == "_":
                if numLefts > 0:
                    return False
                numRights += 1
            if start[pos] == "R" and target[pos] == "R":
                if numLefts > 0:
                    return False
            pos +=1
        
        if numRights>0 or numLefts > 0:
            return False
            
        return True
print(Solution().canChange("_L__R__R_","L______RR"))