class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        size = len(arr) - 1
        pointer = 0
        
        
        while pointer < size and arr[pointer] < arr[pointer + 1]: pointer += 1
            
        if pointer == 0 or pointer == size: return False
        
        while pointer < size and arr[pointer] > arr[pointer + 1] : pointer += 1
            
        return pointer == size