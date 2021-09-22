class Solution:
    def maxLength(self, arr: List[str]) -> int:
        uniq = [""]
        maxi = 0
        for i in range(len(arr)):
            unilen = len(uniq)
            for j in range(unilen):
                sub = arr[i] + uniq[j]
                if len(sub) == len(set(sub)):
                    uniq.append(sub)
                    maxi = max(len(sub),maxi)
        return maxi