class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        rlen = len(image)
        clen = len(image[0])
        
        curcolor = image[sr][sc]
        
        def Backtack(sr,sc):
            
            if (0 > sr) or (rlen-1 < sr) or (0 > sc) or (clen-1 < sc) or (image[sr][sc] != curcolor) or image[sr][sc] == newColor:
                return 
            
            
            image[sr][sc] = newColor
            
            Backtack(sr+1,sc)
            Backtack(sr,sc+1)
            Backtack(sr-1,sc)
            Backtack(sr,sc-1)
            
        
        Backtack(sr,sc)
        
        return image