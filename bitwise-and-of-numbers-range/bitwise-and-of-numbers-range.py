class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:return (m & n & - (2 << math.floor(math.log2(n-m))) if m != n else m)
        