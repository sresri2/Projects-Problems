def ArrayAdditionI(arr):

  arr.sort()
  target = arr[-1]
  arr = arr[0:len(arr)-1]
  if len(arr) > 0 and arr[-1] == target:
    return "true"
  haveArr = [0]
  
  for i in range(0,len(arr)):
    l = len(haveArr)
    for j in range(0,l):
      haveArr.append(haveArr[j]+arr[i])
      lookFor = target - (haveArr[j] + arr[i])
      if lookFor in arr[i+1:]:
        return "true"

  return "false"

  

print(ArrayAdditionI([90,80,11]))