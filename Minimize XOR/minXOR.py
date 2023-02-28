class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        bin1 = bin(num1)[2:]
        bin2 = bin(num2)[2:]
        targetBits = bin2.count("1")
        if targetBits >= len(bin1):
            ret = ""
            for i in range(0,targetBits):
                ret += "1"
            return int(ret,2)
        positions = set()
        pos = 0
        for i in bin1:
            if i == "1":
                positions.add(pos)
            pos += 1
        ret = ""
        added = 0
        pos = 0
        for i in bin1:
            if added<targetBits and pos in positions:
                ret += "1"
                added+=1
            else:
                ret += "0"
            pos += 1
        if added < targetBits:
            dif = targetBits-added
            pos1 = len(ret)-1
            for i in ret[::-1]:
                if i == "0":
                    ret = ret[0:pos1] + "1"+ret[pos1+1:]
                    dif -=1
                    if dif == 0:
                        break
                pos1 -= 1
        return int(ret,2)
        
print(Solution().minimizeXor(65,84))