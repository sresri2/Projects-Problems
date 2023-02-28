class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        org = []
        for i in A:
            org.append(i)

        A.sort()
        B =[]
        for i in A:
            B.append(i)

        A = org
        flipPos = len(A)-1
        maxPos = 0
        kArr = []
        while A != B:
            
            num = max(A) - maxPos

            

            
            if A[0] == num:
                kArr.append(flipPos+1)
                A[0:flipPos+1] = A[0:flipPos+1][::-1]
                maxPos += 1
                flipPos -= 1
            else:
                pos = 0
                for i in A:
                    if i == num:
                        break
                    pos += 1

                A[0:pos+1] = A[0:pos+1][::-1]
                kArr.append(pos+1)

            

        return kArr
        


print(Solution().pancakeSort([3,2,4,1]))


        