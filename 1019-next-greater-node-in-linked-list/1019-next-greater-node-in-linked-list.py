# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        stack = []
        ans = []
        idx = 0
        while head:
            ans.append(0)
            cur_val = head.val
            
            while stack and stack[-1][0] < cur_val:
                last_val = stack.pop()
                ans[last_val[1]] = cur_val
                
            stack.append([cur_val,idx])
            head = head.next
            idx += 1
            
        return ans