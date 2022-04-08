class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        triangle = [[1]]
        for i in range(rowIndex):
            prevrow = triangle[-1]
            midels = [(prevrow[i]+prevrow[i+1]) for i in  range(len(prevrow)-1)]
            cur_row = [1] + midels +[1]
            triangle.append(cur_row)
            
        return triangle[rowIndex]