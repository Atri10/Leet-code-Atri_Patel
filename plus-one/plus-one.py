class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits: s += str(i)
        ans = int(s) + 1
        return list(int(i) for i in str(ans))
        