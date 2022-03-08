class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        
        dummy = n = ListNode(-1)
         
        for i in arr[::-1]:
            node = ListNode(i)
            n.next = node
            n = n.next
        
        return dummy.next
