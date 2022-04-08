class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(numRows-1):
            prevrow = triangle[-1]
            row = [1]
            for i in range(1,len(prevrow)):
                row.append(prevrow[i-1] + prevrow[i])
            row.append(1)
            triangle.append(row)
        return triangle
            
            
