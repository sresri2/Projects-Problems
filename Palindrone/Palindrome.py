def isPalindrome(x):
    q = abs(x)
    revNum = 0 
    while q > 0:
        (q,rem) = divmod(q,10)
        revNum = revNum * 10 + rem
    if revNum == x:
        return True
    return False
    
print(isPalindrome(-121))