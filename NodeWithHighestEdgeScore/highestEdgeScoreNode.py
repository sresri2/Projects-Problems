class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        store = {}
        pos = 0
        for i in edges:
            if i not in store:
                store[i] = [pos]
            else:
                store[i].append(pos)
            pos += 1
                
        ret = None
        cur = None
        for i in list(store.keys()):
            x = sum(store[i])
            if ret == None or x > ret:
                ret = x
                cur = i
                
        return cur

print(Solution().edgeScore([1,0,0,0,0,7,7,5]))