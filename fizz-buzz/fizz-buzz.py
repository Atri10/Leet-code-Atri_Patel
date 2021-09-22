class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [0 * i for i in range(n)]
        for i in range(1,n+1):ans[i-1] = str(i)
        for i in range(2,n,3):ans[i] ="Fizz"
        for i in range(4,n,5):ans[i] ="Buzz"
        for i in range(14,n,15):ans[i] ="FizzBuzz"
        return ans