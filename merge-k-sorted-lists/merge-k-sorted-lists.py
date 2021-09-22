class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        head=n=ListNode(0)
        for node in lists:
            while node:
                arr.append(node.val)
                node = node.next 
        arr = sorted(arr)
        for i in range(len(arr)):
            n.next=ListNode(arr[i])
            n=n.next
        return head.next
        
        

        
   