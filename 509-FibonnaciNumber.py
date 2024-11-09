class Solution:
    def fib(self, n: int) -> int:
        mem = {}

        def helper(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in mem:
                return mem[n]

            mem[n-1] = helper(n-1)
            mem[n-2] = helper(n-2)
            return mem[n-1] + mem[n-2]

        return helper(n)
        
