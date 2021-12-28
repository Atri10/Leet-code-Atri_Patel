class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        lenll = 0
        
        while temp:
            lenll += 1
            temp = temp.next
            
        if lenll % 2 == 0:
            
            temp = head
            
            x = 0 
            
            while temp:
                x += 1
                if x == (lenll // 2) + 1 : return temp
                temp = temp.next
                
        else:
            temp = head
            x = 0 
            
            while temp:
                x += 1
                if x == ((lenll + 1) // 2) : return temp
                temp = temp.next