class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        
        count = 0
        prev = 0
        
        for cur in flowerbed:
            
            if cur == 1 :
                if prev == 1 :
                    count = count - 1
                prev = 1
                
            else:
                
                if prev == 1 :
                    prev = 0
                    
                else:
                    count = count + 1
                    prev = 1
                    
        return count >= n