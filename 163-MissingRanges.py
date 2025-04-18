class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]

        prev = lower - 1
        missing = []
        for n in nums:
            if n - prev > 1:
                missing.append([prev + 1, n - 1])
            prev = n
        
        if upper - prev >= 1:
            missing.append([prev + 1, upper])

        return missing
