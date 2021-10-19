class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            idx=(nums2.index(i))
            arr = nums2[idx+1:]
            if i > max(arr,default=-5):ans.append(-1)
            else:
                for j in arr:
                    if j>i:ans.append(j);break
        return ans