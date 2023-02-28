class Solution(object):
    def topKFrequent(self, nums, k):
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = nums.count(num)

        arr = list(dict.values())
        arr.sort(reverse = True)
        threshold = arr[k-1]


        finalList = []
        for n in dict.keys():
            if dict[n]>=threshold:
                finalList.append(n)

        return finalList

print(Solution().topKFrequent([1,1,1,2,2,3],2))

        
        
