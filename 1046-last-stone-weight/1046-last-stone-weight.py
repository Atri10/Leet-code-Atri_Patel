class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1 :return stones[0]
        
        stones.sort()
        
        x = stones[-1]
        y = stones[-2]
        
        
        while len(stones) > 2:
            
            if x > y:
                stones[-2] = x - y
                stones[-1] = 0
            
            elif x == y:
                stones[-1] = 0
                stones[-2] = 0
                
            for i in stones:
                if i == 0: stones.remove(0)
            
            x = stones[-1]
            y = stones[-2]
            
            stones.sort()
            
        x = stones[-1]
        y = stones[-2]  
        
        if x > y:
                return x-y
        
        return 0
                

        