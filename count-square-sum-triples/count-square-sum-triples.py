class Solution:
    def countTriples(self, n: int) -> int:
        
        ans = 0
        sqrarr = []
        carr = []
        
        for a in range(1,n+1):
            for b in range(1,n+1):
                sqrarr.append(a**2 + b**2)
        
        for c in range(1,n+1):carr.append(c**2)
    
        for i in sqrarr:
            if i in carr:ans +=1
        
        return ans
            
       
            
        