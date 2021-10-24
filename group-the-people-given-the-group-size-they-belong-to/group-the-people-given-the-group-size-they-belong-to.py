class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        ans = []
        for i in range(len(groupSizes)):
            if groupSizes[i] in dic:dic[groupSizes[i]].append(i)
            else:arr = [i];dic[groupSizes[i]] = arr
        for i, (k,v) in enumerate(dic.items()):
            for n in range(0,len(v),k):ans.append(v[n:k+n])
        return ans