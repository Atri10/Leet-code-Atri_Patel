class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def middle(head):
            slow,fast = head,head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def revreslist(head):
            prev = None
            while head:
                nxt_node = head.next
                head.next = prev
                prev , head = head, nxt_node
            return prev
        
        if not head or not head.next : return
        
        left = head.next
        right = revreslist(middle(head))
        i = 0
        
        while left != right:
            if i&1:head.next , left = left, left.next
            else: head.next , right = right, right.next  
            head = head.next
            i += 1
            
            