class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        f, b = 1, 1
        for i in range(1, n+1):        
            if f == 3 and b == 5:            
                s = "FizzBuzz"
                f, b = 0, 0
            elif f == 3:
                s = "Fizz"
                f = 0
            elif b == 5:
                s = "Buzz"
                b = 0
            else:
                s = str(i)

            result.append(s)
            f += 1
            b += 1

        return result
