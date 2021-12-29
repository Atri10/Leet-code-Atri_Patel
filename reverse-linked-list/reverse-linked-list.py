class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        nextt = None
        while head:
            nextt = head.next
            head.next = prev
            prev = head
            head = nextt
        return prev