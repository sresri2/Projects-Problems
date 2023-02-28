# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dict = {}
        pos = 0
        dict[head.val] = pos
        orgHead = head
        canContinue = True
        while canContinue == True and head.next != None:
            pos += 1
            if head.next.val not in dict:
                dict[head.next.val] = pos
            else:
                if head.next.next != None:
                    head.next = head.next.next
                else:
                    head.next = None
            head = head.next
            if head == None:
                canContinue = False
        
        return orgHead




head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)

print(Solution().deleteDuplicates(head))