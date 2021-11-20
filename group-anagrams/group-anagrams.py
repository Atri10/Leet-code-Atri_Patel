class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        mem = {}
        ans = []
        for i in strs:
            temp = ''.join(sorted(i))
            if temp not in mem : mem[temp] = [i]
            else : mem[temp].append(i)
        
        for i in mem.items():ans.append(i[1])
        
        return ans