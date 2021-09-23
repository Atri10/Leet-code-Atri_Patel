class Solution:
    def totalMoney(self, n: int) -> int:
        week  = n//7
        daysremain = n-week*7
        ans = []
        for i in range(1,week+1):
            t = [i for i in range(i,i+7)]
            ans.append(sum(t))
        t = [len(ans)+i+1 for i in range(daysremain)]
        ans.append(sum(t))
        return sum(ans)
       
            