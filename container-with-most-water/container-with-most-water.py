class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0  
        l = 0
        r = len(height)-1
        while l<r:
            maxx = max(maxx,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:l+=1
            else:r-=1    
        return maxx
    