class Solution:
    def countTriples(self, n: int) -> int:return 2*sum(n//(x*x + y*y) for x in range(2, isqrt(n) + 1) for y in range(1, x) if (x&y&1) == 0 and gcd(x,y) == 1)
            
       
            
        