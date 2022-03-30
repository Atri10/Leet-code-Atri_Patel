class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            a = matrix[i]
            if len(a) == 1:
                if a[0] == target :return True
            else :
                l = 0
                r = len(a)-1
                while l <= r :
                    if a[l] == target or a[r] == target:return True
                    l += 1
                    r -= 1
        return False