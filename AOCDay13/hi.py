import functools

def compare(lh, rh):
    if lh == []:
        return 0 if rh == [] else -1
    if rh == []:
        return 1
    if isinstance (lh, list):
        if isinstance (rh, list):
            cmp = compare(lh[0], rh[0])
            if cmp == 0:
                return compare(lh[1:], rh[1:])
            return cmp
        return compare(lh, [rh])
    if isinstance (rh, list):
        return compare([lh], rh)
    return -1 if lh < rh else 1 if rh < lh else 0
    
pairs = [[eval(s) for s in pair.split('\n')] for pair in open("input13.txt").read().split('\n\n')]
items = list(enumerate([item for pair in pairs for item in pair] + ([[[2]], [[6]]])))
N = len(items)-1

items =  sorted(items,
                key=functools.cmp_to_key(lambda lh, rh: compare(lh[1], rh[1])))

print ('Part1', sum(i for i,p in enumerate(pairs, 1)
                    if compare(p[0], p[1])<=0))
print ('Part2', next(idx for idx, (i,_)
                     in enumerate(items, 1) if i == N) *
       next(idx for idx, (i,_)
            in enumerate(items, 1) if i == N-1))