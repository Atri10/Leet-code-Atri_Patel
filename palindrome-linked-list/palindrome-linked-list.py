class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:      
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        node = None 
        
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
            
        while node:
            if node.val != head.val : return False
            node = node.next
            head = head.next
        
        return True