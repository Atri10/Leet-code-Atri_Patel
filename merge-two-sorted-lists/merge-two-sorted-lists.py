# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ar1 = []
        ar2 = []
        while l1:
            ar1.append(l1.val)
            l1 = l1.next
        while l2:
            ar2.append(l2.val)
            l2 = l2.next
        ans = ar1 + ar2
        ans.sort()
        head=n=ListNode(0)
        for i in range(len(ans)):
            n.next = ListNode(ans[i])
            n = n.next
        return head.next
        
        