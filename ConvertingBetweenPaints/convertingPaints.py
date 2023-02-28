def solve(W: int, O: int, B: int, Cow: int, Cbo: int, Cbw: int) -> int:
    """
    Return the minimum cost to convert all of the paint into a single color.
    
    W: non-negative number of buckets of white paint
    O: non-negative number of buckets of orange paint
    B: non-negative number of buckets of brown paint
    Cow: positive cost to convert between a bucket of orange and white paint
    Cbo: positive cost to convert between a bucket of brown and orange paint
    Cbw: positive cost to convert between a bucket of brown and white paint
    """
    possibles = []
    toOrange = (Cbo*B) + (Cow*W)
    toBrown = (Cbo*O) + (Cbw*W)
    toWhite = (Cow*O) + (Cbw*B)
    possibles.append(toOrange)
    possibles.append(toWhite)
    possibles.append(toBrown)

    OBW = ((Cbo*O)+(Cbw*(O+B)))
    Bow = ((Cbo*B)+(Cow*(O+B)))
    BWO = ((Cbw*B)+(Cow*(B+W)))
    WBO = ((Cbw*W)+(Cbo*(B+W)))
    OWB = ((Cow*O)+(Cbw*(W+O)))
    WOB = ((Cow*W)+(Cbo*(O+W)))
    possibles.append(OBW)
    possibles.append(Bow)
    possibles.append(BWO)
    possibles.append(WBO)
    possibles.append(OWB)
    possibles.append(WOB)

    return min(possibles)

def main():
    T = int(input())
    ans = []
    for _ in range(T):
        line = input().split(' ')
        W, O, B = int(line[0]), int(line[1]), int(line[2])
        Cow, Cbo, Cbw = int(line[3]), int(line[4]), int(line[5])
        ans.append(solve(W, O, B, Cow, Cbo, Cbw))
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()