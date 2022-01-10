# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        arr = []
        
        for head in lists:
            while head:
                arr.append(head.val)
                head = head.next
                
        dummy = n = ListNode(-1)
        
        arr.sort()
        
        for i in arr:
            dummy.next = ListNode(i)
            dummy = dummy.next
            
        return n.next