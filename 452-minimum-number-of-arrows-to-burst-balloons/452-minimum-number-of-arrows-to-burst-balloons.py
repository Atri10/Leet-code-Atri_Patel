class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        prev = -float('inf')
        count = 0
        for (x,y) in points:
            if x > prev : 
                count += 1
                prev = y
        return count