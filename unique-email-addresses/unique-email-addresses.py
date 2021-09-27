class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = []
        for i in emails:
            end = i.index("@")
            curloc = i[:end]
            curloc = curloc.replace(".","")
            if "+" in curloc:
                realidx = curloc.index("+")
                curloc = curloc[:realidx]
            curdom = i[end:]
            add = curloc+curdom
            if add not in ans:ans.append(add)
        return len(ans)