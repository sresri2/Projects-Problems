class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        self.pos = []
        num = 0
        self.checkPos = combinationLength-1
        while num < combinationLength:
            self.pos.append(num)
            num += 1
        self.characters = characters
        self.limit = len(characters)-1
        self.combinationLength = combinationLength-1
        self.nextAvailable = True
    def next(self):
        arr = ""
        for i in self.pos:
            arr+=self.characters[i]
        n = self.combinationLength
        for p in self.pos[::-1]:
            self.pos[n]+=1
            if self.pos[n]<=self.limit-(self.combinationLength-n):
                break
            n-=1
        if n<0:
            self.nextAvailable = False
        else:
            posAdjust = self.pos[n]+1
            n+=1
            while n<=self.combinationLength:
                self.pos[n] = posAdjust
                n+=1
                posAdjust+=1
                
        return arr
            
        

    def hasNext(self):
        return self.nextAvailable

combinations = CombinationIterator("abcdef",4)
while combinations.hasNext():
    print(combinations.next())
    print(combinations.hasNext())