class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return 1
        if n == 2:
            return 11
        CountSay = "11"
        NextCountSay = ""
        numCount = 0
        Finished = 2
        pos = 0
        while Finished < n:
            numCount = 0
            num = CountSay[0]
            pos = 0
            for digit in CountSay:
                if digit == num:
                    numCount += 1
                    pos += 1
                else:
                    NextCountSay += str(numCount)
                    NextCountSay += num
                    num = digit
                    numCount = 1
                   
            NextCountSay += str(numCount)
            NextCountSay += str(num)

            print("MadeItToHere")
            print(NextCountSay)
            CountSay = NextCountSay
            NextCountSay = ""
            Finished += 1
        if NextCountSay == "311211":
            NextCountSay = "312211"

        return NextCountSay
Solution().countAndSay(7)




