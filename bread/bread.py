def solve(N: int, K: int, D: int, B: list) -> int:
    """
    Find the maximum amount of bread you can eat before the semester ends, given 
    your available swipes.
    
    N: the number of days in the semester
    K: the number of meal cards you have
    D: the number of days a meal card will be activated for after swiping
    B: the list of integers denoting the number of bread loaves available 
       at the cafeteria on each day
    """
    pos = 0
    subArrs = []
    for i in B:
        subArrs.append(B[pos:pos+D])
        pos += 1
    
    curMax = None
    pos = 0
    for i in subArrs:
        pos1 = 0
        for j in i:
            if j == 0:
                subArrs[pos] = i[0:pos1]
            pos1+=1
        pos += 1
    sums = []
    for i in subArrs:
        if i != []:
            sums.append(sum(i))
    return max(sums)

    
def main():
    T = int(input())
    arr = []
    for _ in range(T):
        N, K, D = (int(x) for x in input().split())
        B = [int(x) for x in input().split()]
        arr.append(solve(N,K,D,B))
    for i in arr:
        print(i)

if __name__ == '__main__':
    main()