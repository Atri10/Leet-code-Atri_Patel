class Solution:
    def numSquares(self, n: int) -> int:
        
        import math
        
        if int(math.sqrt(n))**2==n:return 1
        

        for i in range(int(math.sqrt(n))+1):
            if int(math.sqrt(n-i*i))**2 == n - i*i:return 2
            
            
        for i in range(int(math.sqrt(n))+1):
            for j in range(int(math.sqrt(n))+1):
                    if (n-i*i-j*j) < 0:break
                    if int(math.sqrt(n-i*i-j*j))**2 == (n - i*i - j*j):return 3
                
        return 4