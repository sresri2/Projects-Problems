# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        count = 0
        arr = []
        orgHead = head
        while head:
            count += 1
            arr.append(head.val)
            head = head.next

        stop = count//2 + 1

        done = 0

        pos = 1
        negativePos = 2
        #head = ListNode(arr[0])
        head = orgHead
        print(head.val)
        
        head.next = ListNode(arr[-1])
        head = head.next
        print(head.val)
        for i in arr[1:stop-1]:
            head.next = ListNode(arr[pos])
            head = head.next
            print(head.val)
            head.next = ListNode(arr[-negativePos])
            head = head.next
            print(head.val)
            pos += 1
            negativePos += 1


        if (stop-1) % 2 != 0:
            head.next = ListNode(arr[stop-1])
            print(head.next.val)
            
            
        head = orgHead


        

        


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)



Solution().reorderList(head)
print(head.val)
print(head.next.val)

