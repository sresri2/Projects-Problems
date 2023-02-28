class Solution(object):
    
    def traverse(self,child,A,length,pos):
        nextChild = None
        i = child
        for j in A[pos+1:]:
            if i == j:
                break
            for k in range(2,11):
                if i % k == 0 and j % k == 0:
                    nextChild=j
                    length += 1
                    test = self.traverse(nextChild,A,length,pos+1)
                    if test > length:
                        length = test
                    break
            pos += 1

        return length

    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        pos = 1
        i = A[0]
        children = []
        lengths = []
        for j in A[pos:]:
            for k in range(2,11):
                if i % k ==0 and j % k == 0:
                    child=j
                    length = self.traverse(child,A,2,pos)
                    lengths.append(length)
                    break

            pos += 1
        

        return max(lengths)


print(Solution().largestComponentSize([2,3,6,7,4,12,21,39]))
            
                
        