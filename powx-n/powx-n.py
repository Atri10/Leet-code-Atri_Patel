class Solution:
    def myPow(self, x: float, n: int) -> float:
        from functools import cache
        @cache
        def power(x,n):
            if n==0: return 1
            elif n==1:return x
            elif n < 0: return power(1/x,-n)
            elif n%2==0:return power(x*x,n//2)
            else: return x * power(x*x,(n-1)//2)
            
        return power(x,n)