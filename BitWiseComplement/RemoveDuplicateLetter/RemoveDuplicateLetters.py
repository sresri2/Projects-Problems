class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = set()
        difChars = 0
        for i in s:
            if i not in chars:
                chars.add(i)
                difChars += 1

        numDict = {
            'a': 1,
            'b': 1,
            'c': 1,
            'd': 1,
            'e': 1,
            'f': 1,
            'g': 1,
            'h': 1,
            'i': 1,
            'j': 1,
            'k': 1,
            'l': 1,
            'm': 1,
            'n': 1,
            'o': 1,
            'p': 1,
            'q': 1,
            'r': 1,
            's': 1,
            't': 1,
            'u': 1,
            'v': 1,
            'w': 1,
            'x': 1,
            'y': 1,
            'z': 1
        }
        arr = []
        for i in s:
            arr.append(numDict[i])

        m = min(arr)
        pos = 0
        posStarts = []
        for i in arr:
            if i == m:
                posStarts.append(pos)
        
        find = set()
        for i in posStarts:
            for j in arr[i:]:
                if j not in find:
                    
            
