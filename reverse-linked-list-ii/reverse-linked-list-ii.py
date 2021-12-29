class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ohead = dummy = ListNode(0)
        whead = wtail = head
        dummy.next = head
        for i in range(right - left):wtail = wtail.next
        for i in range(left-1):ohead, whead, wtail = whead,whead.next,wtail.next
        otail = wtail.next
        wtail.next = None
        
        def rev(head):
            pre, cur, tail = None, head, head
            while cur:cur.next, pre, cur = pre, cur, cur.next
            return pre, tail
            
        revhead, revtail = rev(whead)
        ohead.next = revhead
        revtail.next = otail
        return dummy.next