# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        List1Arr = []
        while l1:
            List1Arr.append(l1.val)
            l1 = l1.next

        List2Arr = []
        while l2:
            List2Arr.append(l2.val)
            l2 = l2.next


        List1Arr = List1Arr[::-1]
        List2Arr = List2Arr[::-1]

        num1 = ''
        num2 = ''
        for i in List1Arr:
            num1 += str(i)
        for i in List2Arr:
            num2 += str(i)


        num1 = int(num1)
        num2 = int(num2)

        Sum = num1 + num2
        Sum = str(Sum)
        Sum = Sum[::-1]
        head = ListNode(int(Sum[0]))
        org = head
        pos = 0
        while pos < len(Sum)-1:
            head.next = ListNode(int(Sum[pos+1]))
            head = head.next
            pos += 1


        return org

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(Solution().addTwoNumbers(l1,l2))
