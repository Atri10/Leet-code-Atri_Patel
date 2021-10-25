class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i+1 for i in range(m)]
        ans = []
        for i in range(len(queries)):
            ans.append(P.index(queries[i]))
            P.remove(queries[i])
            P.insert(0,queries[i])
        return ans

        
        
        
        
        