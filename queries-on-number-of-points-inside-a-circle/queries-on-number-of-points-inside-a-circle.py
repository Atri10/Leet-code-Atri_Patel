class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for cricle in queries:
            a = cricle[0]
            b = cricle[1]
            r = cricle[2]
            T = 0
            for point in points:
                LHS = (point[0] - a)**2 + (point[1] - b)**2
                RHS = r**2
                if LHS == RHS or LHS < RHS: T+=1
            ans.append(T)
        return ans
                
        
        