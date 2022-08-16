class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dic = {}
        ans = {}
        for i in nums1:dic[i] = 0
            
        for i in nums2:
            if i in dic:ans[i] = 0
                
        return list(ans.keys())