class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                dummy.next = l2
                l2 = l2.next
            else:
                dummy.next = l1
                l1 = l1.next
            dummy = dummy.next
        dummy.next = l1 or l2
        return head.next