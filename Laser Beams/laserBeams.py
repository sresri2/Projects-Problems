class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        pos = 0
        DeviceDict = {}
        NoDevice = set()
        curLink = []
        links = []
        for row in bank:
            if str(int(row))[0]=="0":
                DeviceDict[pos] = 0
                NoDevice.add(pos)

            else:   
                DeviceDict[pos] = row.count("1")
                curLink.append(pos)
                if len(curLink) == 2:
                    links.append(curLink)
                    curLink = []
                    curLink.append(pos)
            pos += 1
        if links == []:
            return 0
        lasers = 0
        for i in links:
            lasers += (DeviceDict[i[0]]*DeviceDict[i[1]])
        return lasers

print(Solution().numberOfBeams(["000","111","000"]))
        

