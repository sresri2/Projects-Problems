class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if "1" not in s:
            return len(s) 
        firstOneFound = False
        cur = ""
        endZs = 0
        for i in s[::-1]:
            '''
            if not firstOneFound:
                if i == "1":
                    firstOneFound = True
                    cur += i
                else:
                    endZs += 1
            '''
            if i == "1":
                x = cur+i
                x = x[::-1]
                x = int(x,2)
                if x <= k:
                    cur = bin(x)
                    cur = cur[2:]
                    cur = cur[::-1]
            elif i == "0":
                cur += i
        '''
        done = 0
        cur = cur[::-1]
        print(cur)
        while done < endZs:
            x = cur+"0"
            if int(x,2)<= k:
                cur += "0"
            else:
                break
            done += 1
        '''
        return len(cur)
        
print(Solution().longestSubsequence("1001011100000010111111110011000100011101100110100001001100110110001111000110111011010110000",205790338))
print(int("00000000000000000000000000000001100011110001101110110101100",2))
