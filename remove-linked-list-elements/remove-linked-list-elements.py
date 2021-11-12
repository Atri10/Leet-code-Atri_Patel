class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
            if not head: return
            if head.val == val : return self.removeElements(head.next,val)
            head.next = self.removeElements(head.next,val)
            return head