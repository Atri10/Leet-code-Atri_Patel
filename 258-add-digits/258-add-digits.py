class Solution:
    def addDigits(self, num: int) -> int:
        def rec(n):
            x = str(n)
            s = sum([int(i) for i in x])
            if s < 10 : return s
            return rec(s)
        return rec(num)