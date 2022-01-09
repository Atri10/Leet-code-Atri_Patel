# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = {}
        while head:
            v = head.val
            if v in stack : stack[v] = stack[v] + 1
            else : stack[v] = 1
            head = head.next
            
        dummy = n = ListNode(-1)
        for (k,v) in stack.items():
            if v == 1 : 
                dummy.next = ListNode(k)
                dummy = dummy.next
        return n.next