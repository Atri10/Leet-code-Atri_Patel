class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s.split())
        a = list(reversed(s))
        return " ".join(a)