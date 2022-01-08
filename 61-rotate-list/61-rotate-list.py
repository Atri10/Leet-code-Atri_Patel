# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next : return head
        
        dummy = head
        n = 1
        
        while dummy.next:
            dummy = dummy.next
            n += 1
            
        if k % n == 0 : return head
        
        middle = head
        
        for i in range(n - k%n-1):
            middle = middle.next
            
        new = middle.next
        dummy.next = head
        middle.next = None
        
        return new
        
        
        