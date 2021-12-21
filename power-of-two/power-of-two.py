class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def rec(n):
            if n==0 : return False
            elif n==1 or n==2: return True
            elif n %2 != 0 : return False
            return rec(n//2)
        return rec(n)