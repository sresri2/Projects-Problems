class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        for query in queries:
            arr = []
            store = {}
            counts = {}
            pos = 0
            for i in nums:
                arr.append(i[len(i)-query[1]:])
                if arr[pos] not in store:
                    store[arr[pos]] = [pos]
                    counts[arr[pos]] = 1
                else:
                    store[arr[pos]].append(pos)
                    counts[arr[pos]] += 1
                pos += 1
            
            
            
        return ret

print(Solution().smallestTrimmedNumbers(["24","37","96","04"],[[2,1],[2,2]]))