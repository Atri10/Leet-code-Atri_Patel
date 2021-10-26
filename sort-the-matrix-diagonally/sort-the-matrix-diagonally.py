class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dic = {}
        ans = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i-j not in dic: 
                    dic[i-j] = [mat[i][j]]
                else: dic[i-j].append(mat[i][j])
                    
        for (k,v) in dic.items(): ans[k] = sorted(v)
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):mat[i][j] = ans[i-j].pop(0)
        return mat