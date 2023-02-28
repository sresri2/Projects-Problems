import fileinput
def calculate(n, pos):
    repeat = n-pos+1
    extrasteps = (repeat-1)*(n-pos)
    if pos == n:
        return 0
    return (extrasteps+(repeat*(calculate(n,pos+1)+1)))

for line in fileinput.input():
    n = int(line.strip())
    break
if n ==1:
    print(0)
else:   
    print(calculate(n,2)+1)
