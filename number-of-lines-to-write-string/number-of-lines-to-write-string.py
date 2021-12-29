class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        c = 0
        for i in s:
            c += widths[ord(i)-97]
            if c>100:
                line += 1
                c = widths[ord(i)-97]
        return [line,c]