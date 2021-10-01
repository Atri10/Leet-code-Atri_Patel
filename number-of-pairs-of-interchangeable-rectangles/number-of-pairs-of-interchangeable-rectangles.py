from collections import Counter
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ans = 0
        items = {}
        for i in rectangles:
            ratio = i[0]/i[1]
            if ratio in items:
                if items[ratio] == 1:ans += 1
                else: ans += items[ratio]
                items[ratio] += 1
            else:items[ratio] = 1
        return ans
            