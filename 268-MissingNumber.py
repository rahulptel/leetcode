class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        ideal = (n*(n+1))/2

        return int(ideal - s)
