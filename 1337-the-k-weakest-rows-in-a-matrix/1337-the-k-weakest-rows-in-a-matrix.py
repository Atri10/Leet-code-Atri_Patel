class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        dic = {}
        
        for i in range(len(mat)):
            
            dic[i] = mat[i].count(1)
    
    
        dic = sorted(dic.items() ,key = lambda x : x[1])
        
        ans = [dic[i][0] for i in range(k)]
        
        return ans