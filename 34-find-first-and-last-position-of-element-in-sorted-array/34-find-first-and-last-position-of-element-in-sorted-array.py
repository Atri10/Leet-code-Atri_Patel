class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        def startBS(arr,k):
            
            l = 0
            r = len(arr)-1
            idx = - 1
            while l <=r:
                mid = (l+r)//2
                if arr[mid] == k : 
                    idx = mid
                if arr[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return idx
        
        
        def endBS(arr,k):
            l = 0
            r = len(arr)-1
            idx = - 1
            while l <=r:
                mid = (l+r)//2
                if arr[mid] == k : 
                    idx = mid
                if arr[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            return idx
        
        return [startBS(nums,target),endBS(nums,target)]