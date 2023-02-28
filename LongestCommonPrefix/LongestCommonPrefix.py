def longestCommonPrefix(strs):
    if strs == []:
        return ""
    comPre = strs[0]
    #pos = 0
    
    for word in strs[1:]:
        while (len(comPre)>0):
            if word.startswith(comPre):
                break
            comPre = comPre[0:(len(comPre)-1)]
        if len(comPre) == 0:
            break
    return comPre
    """
        comPre = ""
        pos = 0
        for letter in strs[0]:
        for word in strs:
            if pos > len(word) - 1:
                print(comPre)
                return comPre
            if letter != word[pos]:
                print(comPre)
                return comPre
        comPre+=letter
        pos += 1
    print(comPre)
    """
print(longestCommonPrefix(["flower", "floor", "flag"]))
        


                

    
            

    

    

"""
Store common prefix as empty
pos: set as 0
Loop through letters of the first item: for letter in item[0]
    Loop through all other words: for word in words
        Compare with corresponding letter of that word: word[pos] with letter
        If one of them does'nt have the same first letter, then return the current common prefix
    If all of them have the same letter, then add the letter to the common prefix 
    increment pos


"""

    