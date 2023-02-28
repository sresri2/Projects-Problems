class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        if len(beans)<=1:
            return 0
        beans.sort()
        total = 0
        store = {}
        pos = 0
        for i in beans:
            total += i
            store[pos]=total
            pos += 1


        minRemove = None
        pos = 0
        count = 0
        x = len(beans)
        while pos <len(beans):
            if not minRemove:
                minRemove = total-store[pos]
            else:
                num = total-store[pos-1]
                y = x-pos-1
                z = beans[pos]
                y*=z
                num-=z
                num-=y
                num += store[pos-1]
                if num < minRemove:
                    minRemove=0
                    minRemove+= num
            pos += 1
        return minRemove

print(Solution().minimumRemoval([4,1,6,5]))

            
