class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        j = 0
        ans = 0
        for i in columnTitle[::-1]:
            ans += ((ord(i) - ord("A") +1) * 26**j )
            j +=1
        return ans