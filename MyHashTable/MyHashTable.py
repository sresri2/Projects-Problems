class MyHashSet(object):

    def __init__(self):
        self.searchDict = []        
        pos = 0

        while pos < 10000:
            self.searchDict.append([])
            pos += 1

    def add(self, key):
        posInDict = key//10000

        self.searchDict[posInDict].append(key)
        

    def remove(self, key):
        listInDict = self.searchDict[key//10000]

        pos = 0
        for num in listInDict:
            if num == key:
                del(listInDict[pos])
            pos += 1
        

    def contains(self, key):
        if key in self.searchDict[key//10000]:
            return True
        else:
            return False