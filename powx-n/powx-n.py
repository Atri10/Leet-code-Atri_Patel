class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        memo = {}
        
        def power(x,n):
            if n in memo:return memo[n]

            if n==0: return 1
            elif n==1:return x
            elif n < 0:
                memo[n] = power(1/x,-n)
                return memo[n]
            elif n%2==0:
                memo[n] = power(x*x,n//2)
                return memo[n]
            else:
                memo[n] = x * power(x*x,(n-1)//2)
                return memo[n]
            
        return power(x,n)