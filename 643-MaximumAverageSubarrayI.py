class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = sum(nums[:k])
        result = sum_
        if len(nums) == k:
            return sum_ / k

        for i in range(k, len(nums)):            
            sum_ = sum_ - nums[i - k] + nums[i]
            result = max(result, sum_)
            
        return result / k
