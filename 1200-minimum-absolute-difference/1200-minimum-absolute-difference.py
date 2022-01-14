class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        
        arr.sort()
        ans = []
        minn = float('inf')        
        
        for i in range(len(arr)):
            a,b = sorted((arr[i],arr[i-1]))
            diff = b - a
            
            if minn > diff : 
                minn = diff
                ans = [[a,b]]
                
            elif minn == diff : 
                ans.append([a,b])
            
        
        return ans