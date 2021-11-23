class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        row = [1]
        triangle.append(row)
        if numRows == 1 : return triangle
        
        for i in range(1,numRows):
            prevrow = triangle[-1]
            cur_row = [1]
            for j in range(len(prevrow)-1):cur_row.append(prevrow[j] + prevrow[j+1])
            cur_row.append(1)
            triangle.append(cur_row)
            
        return triangle