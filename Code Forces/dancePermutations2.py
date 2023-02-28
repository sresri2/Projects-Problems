import itertools
from itertools import permutations
import fileinput
for line in fileinput.input():
    n = int(line.strip())
    break

ar = []
for i in range(1,n+1):
    ar.append(i)
print(list(permutations(ar,n)))
