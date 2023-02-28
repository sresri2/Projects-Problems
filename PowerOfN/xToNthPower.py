class Solution(object):
    def myPow(self, x, n):
        if x == 1 or n == 0:
            return 1
        orgX = x
        multiply = 10
        if n > 0:
            done = 1
            while done < n:
                if (done*multiply)<n:
                    x = x * x * x * x * x * x * x * x * x * x * x 
                    done = done*multiply
                else:
                    x = x * orgX
                    done+=1
                    multiply = int(multiply/2)

            return x

        if n < 0:
            x = 1/x**-n
            return x

print(Solution().myPow(0.00001,2147483647))