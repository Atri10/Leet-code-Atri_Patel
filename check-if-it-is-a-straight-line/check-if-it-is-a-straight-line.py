class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (a,b) , (c,d) = coordinates[:2]
        for x,y in coordinates:
            if (y-d)*(c-a) != (x-c)*(d-b) : return False
        return True