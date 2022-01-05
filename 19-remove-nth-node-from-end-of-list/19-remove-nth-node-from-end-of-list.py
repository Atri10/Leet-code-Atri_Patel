# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        lenn = 0
        
        while temp:
            
            temp, lenn = temp.next, lenn + 1
        
        if lenn == n : return head.next
            
        temp = head
        
        for i in range(1,lenn-n):
            
            temp = temp.next
            
        temp.next = temp.next.next
        
        return head