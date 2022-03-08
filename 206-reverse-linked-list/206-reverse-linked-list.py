class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        prev = None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next 
            
        return prev