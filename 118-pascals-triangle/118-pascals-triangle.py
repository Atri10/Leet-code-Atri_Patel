class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        triangle = []
        
        
        triangle.append([1])
        triangle.append([1,1])
        
        if numRows < 3:
            return triangle[:numRows]
        
        for i in range(3,numRows+1):
            
            prevrow = triangle[-1]
            
            cur = []
            cur.append(1)
            for k in range(len(prevrow)-1):
                cur.append(prevrow[k] + prevrow[k+1])
            
            cur.append(1)
            triangle.append(cur)
   

        return triangle