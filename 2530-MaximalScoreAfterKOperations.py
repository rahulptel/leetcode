from heapq import heapify, heapreplace
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
                        
        heapify(nums)
        cnt = 0
        while k:
            cnt += nums[0]                        
            heapreplace(nums, math.floor(nums[0] / 3))
            k -= 1

        return -cnt
        
