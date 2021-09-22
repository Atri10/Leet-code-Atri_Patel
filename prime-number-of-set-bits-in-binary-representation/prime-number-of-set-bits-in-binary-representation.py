class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        pset = [2,3,5,7,11,13,17,19]
        for i in range(left,right+1):
            b = bin(i)
            b = b[2:]
            p = b.count("1")
            if p in pset:ans+=1
        return ans
        