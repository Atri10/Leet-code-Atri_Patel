class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)
        lc = 0
        lcost = 0
        rc = 0
        rcost = 0
        for i in range(1,len(boxes)): 
            if boxes[i-1]=="1": lc+=1
            lcost += lc
            ans[i] = lcost
        for i in range(len(boxes)-2,-1,-1):
            if boxes[i+1]=="1": rc+=1
            rcost += rc
            ans[i] += rcost
        return ans