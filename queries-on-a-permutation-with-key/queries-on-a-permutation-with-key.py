class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = []
        ans = []
        for i in range(m):P.append(i+1)
        for i in range(len(queries)):
            el = queries[i]
            ans.append(P.index(el))
            P.remove(el)
            P.insert(0,el)
        return ans

        
        
        
        
        