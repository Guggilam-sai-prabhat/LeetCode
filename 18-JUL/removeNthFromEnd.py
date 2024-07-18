# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        first = head 
        for i in range(n):

            if first == None:
                return None
            first = first.next 

        second = head 
        prev = None  # track the previous node of second

        while first != None:
            prev = second
            second = second.next
            first = first.next

        if prev == None:  # special case: n is the length of the list
            return head.next
        else:
            prev.next = prev.next.next

        return head
