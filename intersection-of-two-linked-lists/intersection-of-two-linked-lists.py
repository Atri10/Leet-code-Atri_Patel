# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        lenA = 0
        lenB = 0
        
        tempA = headA
        tempB = headB
        
        while tempA:
            lenA += 1
            tempA = tempA.next
        
        while tempB:
            lenB += 1
            tempB = tempB.next
            
       
        diff = abs(lenA-lenB)
        
        if lenA > lenB:
            
            i = 0
            while headA:
                i += 1
                headA = headA.next
                if i == diff : break
                
                
        elif lenA < lenB:
            
            i = 0
            while headB:
                i += 1
                headB = headB.next
                if i == diff : break
                
                
        p1 = headA
        p2 = headB
        
        
        
        while p1 and p2:
            if p1 == p2 : return p1
            else : 
                p1 = p1.next
                p2 = p2.next
            
            
                
       