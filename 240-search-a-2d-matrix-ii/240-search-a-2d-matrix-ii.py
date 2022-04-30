class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def BS(arr,val): 
            l = 0
            r = len(arr) - 1     
            while r >= l:
                mid = (l+r) // 2
                if arr[mid] == val :return mid 
                if arr[mid] < val:l = mid + 1
                else:r = mid - 1
            return -1
        
        for i in matrix:
            if BS(i,target) != -1 : return True