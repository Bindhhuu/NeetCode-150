class Solution:
    def climbStairs(self, n: int) -> int:
        '''memo = {1:1, 2:2}
        def f(n):
            if n in memo:
                return memo[n]
            else :
                memo[n] = f(n-2) + f(n-1)
                return memo[n]
            
        return f(n) '''

        if n == 1:
            return 1
        a, b = 1, 2

        for i in range(3, n+1):
            a, b = b, a+b
        return b

    
