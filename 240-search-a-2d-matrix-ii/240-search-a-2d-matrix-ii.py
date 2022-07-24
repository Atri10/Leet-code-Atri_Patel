class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rlen = len(matrix[0])-1
        
        def BS(row):
            l = 0
            r = rlen
            while l <= r:
                mid = (l+r)//2
                cuel = row[mid]
                if cuel == target : return True
                elif cuel > target: r = mid - 1
                else: l = mid + 1
            
            return False
        
        
        
        for row in matrix:
            if BS(row):
                return True