sortedArr = []
def mergeTwoLists(l1, l2):
    for num in l1:
        for item in l2:
            if num < item:
                sortedArr.append(num)
                break
            if item <= num:
                sortedArr.append(item)
    print(sortedArr)
    return sortedArr

mergeTwoLists([1,3,5,7],[2,4,6,8])

