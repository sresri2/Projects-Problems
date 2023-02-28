# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        prev = head
        orgHead = head
        if not head:
            return None
        if not head.next:
            if head.val == val:
                orgHead = None
                return orgHead
        
        while head.val == val:
            orgHead = head.next
            prev = head.next
            head = head.next
            if orgHead == None:
                return None
    
        while head:
            if head.val == val:
                head = head.next
                prev.next = head
            else:
                prev = head
                head = head.next

        return orgHead


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)


print(Solution().removeElements(head,3))