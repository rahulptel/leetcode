import math

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeros, ones = 0, 0        
        for idx, bed in enumerate(flowerbed):
            if bed == 0:
                zeros += 1
            
            if bed == 1:
                ones += 1
                if zeros - ones > 0:
                    n -= math.ceil((zeros - ones)/2)
                    if n <= 0:
                        return True

                ones = 1
                zeros = 0


        if zeros - ones > 0:
            n -= math.ceil((zeros - ones)/2)
        
        if n > 0:
            return False
        
        return True
        
