class Solution:
    def totalMoney(self, n: int) -> int:
        week  = n//7
        daysremain = n-week*7
        ans = 0
        for i in range(1,week+1):
            ans+=sum(range(i,i+7))
        t = [week+i+1 for i in range(daysremain)]
        ans +=sum(t)
        return ans
       
            