class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        N = bin(N)
        pos = 0
        N = N[2:]
        for i in N:
            if i == "1":
                N = N[0:pos] + "0" + N[pos+1:]
            else:
                N = N[0:pos] + "1" + N[pos+1:]
            pos += 1
        return int(N,2)


print(Solution().bitwiseComplement(10))
