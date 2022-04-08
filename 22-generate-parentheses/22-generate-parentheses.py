class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def BackTrack(nopen,nclose,path):
            if n == nclose:
                ans.append(path)
                return
            if n > nopen:BackTrack(nopen+1,nclose,path+ "(")
            if nopen > nclose: BackTrack(nopen,nclose + 1,path+ ")")
                
        
        BackTrack(0,0,"")
        return ans