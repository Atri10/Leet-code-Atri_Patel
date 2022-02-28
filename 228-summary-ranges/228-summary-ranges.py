class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        n = len(nums)
        if n == 0 : return []
        arr = []
        a = nums[0]
        for i in range(len(nums)):
            
            if (i == n-1) or (nums[i] + 1 != nums[i+1]):
                
                if nums[i] != a:
                    strr = str(a) + "->" + str(nums[i])
                    arr.append(strr)
                    
                else:
                    arr.append(str(a))
                    
                
                if i != n- 1:
                    a = nums[i+1]
                    
        return arr