class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        dic = {}
        
        for i in nums2[::-1]:
            
            while stack and i > stack[-1]:
                stack.pop()
                
            if stack:
                dic[i] = stack[-1]
                
            stack.append(i)
            
        
        ans = []
        
        for i in nums1:
            
            if i in dic:
                ans.append(dic[i])
            else:
                ans.append(-1)
        
        return ans
                