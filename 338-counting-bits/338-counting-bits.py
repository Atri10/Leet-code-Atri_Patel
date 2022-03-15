class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        
        def countsetbits(n):
            c = 0
            while n:
                c += n&1
                n = n >> 1
            return c
        
        for i in range(0,n+1):arr.append(countsetbits(i))
        return arr