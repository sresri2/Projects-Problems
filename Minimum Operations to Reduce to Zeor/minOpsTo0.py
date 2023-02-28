class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while True:
            cur = 2 ** i
            if cur == n:
                return 1
            if cur > n:
                lesser = cur/2
                greater = cur
                break
            i += 1
                
        up = n
        need = 0
        while up != greater:
            i = 0
            while True:
                cur = 2 ** i
                if up + cur == greater:
                    need += 1
                    break
                if up + cur > greater:
                    cur /= 2
                    need += 1
                    break
                i += 1
            up += cur
        
        need1 = need
        up = lesser
        need = 0
        while up != n:
            i = 0
            while True:
                cur = 2 ** i
                if up + cur == n:
                    need += 1
                    break
                if up + cur > n:
                    cur /= 2
                    need += 1
                    break
                i += 1
            up += cur
        return min(need,need1) + 1

print(Solution().minOperations(39))