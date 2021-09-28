class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        ans = []
        for i in nums:
            if i%2==0:even.append(i)
            else:odd.append(i)
        for i in range(len(nums)):
            if i%2==0:ans.insert(i,even[i//2])
            else:ans.insert(i,odd[i//2])
        return ans