class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxx = 0  
        l = 0
        r = len(height)-1
        
        while l<r:
            area = min(height[l],height[r])*(r-l)
            maxx = max(maxx,area)
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1  
                
        return maxx