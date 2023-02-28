class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        plusPos = 0
        for i in expression:
            if i == "+":
                break
            plusPos += 1
        
        curMin = None
        pos = 0
        for i in expression[0:plusPos]:
            pos1 = 0
            for j in expression[plusPos+1:]:
                str1 = expression[0:pos]
                str2 = expression[pos:plusPos]
                str3 = expression[plusPos+1:pos1+1]
                str4 = expression[pos1+1:]
                int1 = 1
                if str1 != "":
                    int1 = int(str1)
                int2 = 0
                if str2 != "":
                    int2 = int(str2)
                int3 = 0
                if str3 != "":
                    int3 = int(str3)
                int4 = 1
                if str4 != "":
                    int4 = int(str4)

                
                x = int1 * (int2 + int3) * int4
                
                if not curMin:
                    curMin = x
                elif x < curMin:
                    curMin = x
                pos1 += 1
            pos += 1
        return curMin
 