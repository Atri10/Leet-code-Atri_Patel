class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = []
        even = 0
        odd = 1
        for i in nums:
            if i%2==0:ans.insert(even,i);even +=2
            else:ans.insert(odd,i);odd +=2
        return ans