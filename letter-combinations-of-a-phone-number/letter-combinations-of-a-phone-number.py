class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return []
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []
        def DFS(nums,idx,path,ans):
            if idx >= len(nums):
                ans.append(path)
                return
            string  = dic[nums[idx]]
            for i in string:DFS(nums,idx+1,path+i,ans)
            
        DFS(digits,0,"",ans)
        
        return ans
            
            
        
            
                
            
        
            
        
        
        
      