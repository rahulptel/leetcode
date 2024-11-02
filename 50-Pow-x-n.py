class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        x = x if n>0 else (1/x)
        n = n if n>0 else abs(n)
        
        def calculate_power(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            n1 = int(n/2)
            n2 = n - 2*n1
            result = calculate_power(x, n1)            
            return result*result*calculate_power(x, n2)


        return calculate_power(x, n)

