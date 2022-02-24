# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        l = []
        
        while head:
            l.append(head.val)
            head = head.next
        
        dummy = n = ListNode(0)
        l.sort()
        
        for i in l:
            n.next = ListNode(i)
            n = n.next
            
        return dummy.next