class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = []
        p = []
        z = []
        res = set()  
        for i in nums:
            if i>0:p.append(i)
            elif i==0:z.append(i)
            else:n.append(i)
        N,P = set(n),set(p)
        if z:
            for i in P:
                if -1*i in N:res.add((-1*i,0,i))
        if len(z)>=3:res.add((0,0,0))
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                T = -1*(n[i]+n[j])
                if T in P : res.add(tuple(sorted([n[i],n[j],T])))
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                T = -1 * (p[i]+p[j])
                if T in N: res.add(tuple(sorted([p[i],p[j],T]))) 
        return res
            