
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    pos = len(digits)-1
    for item in digits[::-1]:
        if item == 9:
            if pos > 0:
                item = 0
                digits[pos]=0
                pos -= 1
            else:
                digits[pos]=1
                for item in digits:
                    item = 0
                    break
                digits.append(0)
                break
        else:
            item +=1
            digits[pos] +=1
            break
    print(digits)
    return digits
plusOne([9,9])




            