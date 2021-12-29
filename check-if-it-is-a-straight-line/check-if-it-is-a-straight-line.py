class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        a,b = coordinates[0]
        c,d = coordinates[1]
        
        if c-a  == 0 : ogslop = float('inf')
        else:ogslop = int((d-b) // (c-a))
        
        for i in range(1,len(coordinates)-1):
            a,b = coordinates[i]
            c,d = coordinates[i+1]
            
            if c-a  == 0 : slop = float('inf')
            else:slop = int((d-b) // (c-a))
            
            if slop != ogslop : return False
            
        return True