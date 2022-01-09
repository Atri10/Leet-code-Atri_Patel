class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        temp =  head
        while temp:
            arr.append(temp)
            temp = temp.next
            
        l = 1
        r = len(arr) - 1
        
        for i in range(len(arr)):
            if i & 1 :
                head.next = arr[l]
                l += 1
            else :
                head.next = arr[r]
                r -= 1
                
            head = head.next
            
        head.next = None