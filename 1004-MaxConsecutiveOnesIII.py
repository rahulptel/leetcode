class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            k = k if nums[right] == 1 else k - 1
            if k < 0:
                k = k+1 if nums[left] == 0 else k
                left += 1

        return right - left + 1
        
