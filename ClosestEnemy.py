def ClosestEnemy(arr):
  if 2 not in arr:
    return 0
  onePos = arr.index(1)
  pos = onePos
  leftDist = len(arr) + 1
  rightDist = len(arr) + 1
  for i in arr[onePos:]:
    if i == 2:
      rightDist = pos - onePos
      break
    pos += 1
  pos = onePos - 1
  for i in arr[0:onePos][::-1]:
    if i == 2:
      leftDist = onePos-pos
      break
    pos -= 1
  
  return min(leftDist,rightDist)
print(ClosestEnemy([2,0,0,0,0,0,1,0,0,0,0,0,2]))