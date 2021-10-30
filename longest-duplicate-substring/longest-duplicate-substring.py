class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ln=len(s)
        
        mod=2**63-1
        a=ord('a')
        arr=[ord(ch)-a for ch in s]
        def has_duplicate_slen_substring2(slen):
            highest_digit=(26**slen)%mod
            #get the hash value of the first substring of length slen
            val=0
            for i in range(slen):
                val=(val*26+arr[i])%mod            
            seen=set([val])
            
            for i in range(slen, ln):
                val=(val*26+arr[i]-arr[i-slen]*highest_digit)%mod
                if val in seen:
                    return i-slen+1 #start index of the repeat string
                seen.add(val)
            return 0 #not found repeat string
                    
        def has_duplicate_slen_substring(slen):
            tracker=set()
            for i in range(ln-slen+1):
                substring=s[i:slen+i]
                if substring in tracker:
                    return i
                tracker.add(substring)
            return 0
                
        
        start=0
        lo=1 #minimal len
        hi=ln #max len
        while lo<hi:
            mi=(lo+hi)//2
            pos=has_duplicate_slen_substring(mi)
            if pos:
                start=pos
                lo=mi+1
            else:
                hi=mi
        return s[start:start+lo-1]