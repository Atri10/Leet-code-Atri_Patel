class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points)
        diff = 0
        for i in range(len(points)-1):
            a = points[i]
            b = points[i+1]
            c = abs(a[0]-b[0])
            if c > diff: diff = c
        return diff