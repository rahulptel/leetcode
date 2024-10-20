class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def cnt_ways(state):
            if state in mem:
                return mem[state]

            if state > n:
                return 0

            if state == n or state == n-1:
                return 1

            mem[state+1] = cnt_ways(state+1)
            mem[state+2] = cnt_ways(state+2)
            return mem[state+1] + mem[state+2]
        
        return cnt_ways(0)

        
