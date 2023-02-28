class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        buckets = []
        done = 0
        while done < 1000:
            buckets.append([])
            done += 1
            
        posDict = {}
        pos = 0
        for i in nums:
            if i not in posDict:
                posDict[i]= [pos]
            else:
                posDict[i].append(pos)
            pos += 1
        for i in nums:
            buckets[int(i/10)].append(i)
            need = abs(t - i)
            for j in buckets[int(need/10)]:
                if j <= need:
                    for pos in posDict[i]:
                        for pos2 in posDict[j]:
                            if abs(pos-pos2) <= k:
                                return True


        return False


print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))