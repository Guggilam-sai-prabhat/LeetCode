# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if(list1==None):
            return list2
        if (list2==None):
            return list1
        head = None
        tail = None
        
        if(list1.val<=list2.val):
            head = tail = list1
            list1 = list1.next
        else:
            head = tail = list2
            list2 = list2.next
        
        while(list1!=None and list2!=None):
            if(list1.val<=list2.val):
                tail.next = list1
                tail  = list1
                list1 = list1.next
            else:
                tail.next = list2
                tail = list2
                list2 = list2.next
        if(list1 == None):
            tail.next = list2
        else:
            tail.next = list1
        print(list1,list2)
        return head
                
        
        
        
