def minimumOperations(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxOccurEven = None
    secEven = None
    evenCounts = {}
    totalEven = 0
    maxOccuringNum = None
    for i in nums[::2]:
        if i not in evenCounts:
            evenCounts[i]=1
        else:
            evenCounts[i]+=1
        if maxOccurEven == None:
            maxOccuringNum = i
            maxOccurEven = evenCounts[i]
        elif evenCounts[i]>maxOccurEven:
            if i != maxOccuringNum:
                secEven = maxOccurEven
                maxOccuringNum = i
            maxOccurEven = evenCounts[i]
        totalEven+=1
    
    maxOccurOdd = None
    secOdd = None
    maxOccuringNum2 = None
    oddCounts = {}
    totalOdd = 0
    for i in nums[1::2]:
        if i not in oddCounts:
            oddCounts[i]=1
        else:
            oddCounts[i]+=1
        if maxOccurOdd == None:
            maxOccurOdd = oddCounts[i]
            maxOccuringNum2 = i
        elif oddCounts[i]>maxOccurOdd:
            if i != maxOccuringNum2:
                secOdd = maxOccurOdd
                maxOccuringNum2 = i
            maxOccurOdd = oddCounts[i]
        totalOdd+=1
    if maxOccuringNum == maxOccuringNum2:
        if totalEven>=totalOdd:
            maxOccurOdd = secOdd
        else:
            maxOccurEven = secEven
    
    return (totalEven-maxOccurEven)+(totalOdd-maxOccurOdd)


