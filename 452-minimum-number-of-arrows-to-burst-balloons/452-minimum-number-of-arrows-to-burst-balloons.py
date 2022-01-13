class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        prev = -float('inf')
        count = 0
        for p in points:
            if p[0] > prev : 
                count += 1
                prev = p[1]
        return count