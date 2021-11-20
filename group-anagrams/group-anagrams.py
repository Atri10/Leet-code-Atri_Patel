class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        ans = []
        for i in strs:
            temp = ''.join(sorted(i))
            mem[temp].append(i)
            
        for i in mem.items():ans.append(i[1])
        return ans