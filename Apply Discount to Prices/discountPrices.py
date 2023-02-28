import string
class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        letters = set(string.ascii_lowercase)
        words = sentence.split()
        pos = 0
        for i in words:
            if i[0]=="$":
                if len(i)>1:
                    if i[1] != "0":  
                        try:
                            num = float(i[1:])
                            x = True
                        except:
                            x= False
                        if x:
                            num = float(i[1:])
                            num = str(float(num)*float(1-(discount/100)))
                            words[pos] = ("$" + "%.2f" %float(num))
            pos +=1
        pos = 0
        newSentence = ""
        for i in words:
            newSentence += i
            if pos < len(words)-1:
                newSentence += " "
        return newSentence

print(Solution().discountPrices("there are $1 $2 and 5$ candies in the shop",50))