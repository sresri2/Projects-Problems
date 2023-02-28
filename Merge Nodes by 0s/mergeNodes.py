# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        org = head
        curSum = 0
        store = None
        while head != None:
            if head.val == 0:
                if store:
                    store.next.val = curSum
                    store.next.next = head
                    curSum = 0
                    store = head
                else:
                    store = head
            else:
                curSum += head.val
            head = head.next
        head = org
        storeHead = head
        prev = None
        while head != None:
            if head.val != 0 and not prev:
                prev = head
                ret = prev
            elif head.val != 0 and prev != None:
                prev.next = head
                prev = head
            head = head.next
            if not head:
                prev.next = None
        
        return ret


head = ListNode(0)
head.next = ListNode(3)
head.next.next = ListNode(1)
head.next.next.next = ListNode(0)
print(Solution().mergeNodes(head))
