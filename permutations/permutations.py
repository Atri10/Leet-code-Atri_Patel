class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def DFS(nums,path,res):
            if len(nums)==0:res.append(path)
            for i in range(len(nums)):
                DFS(nums[i+1:]+nums[:i] ,path+[nums[i]],res)
                
        DFS(nums,[],res) 
        return (res)