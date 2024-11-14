class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = nums[0] if nums[0] > 0 else 0
        for j in range(1, len(nums)):
            currsum += nums[j]
            
            if currsum > maxsum:
                maxsum = currsum

            if currsum < 0:
                currsum = 0
                        
        return maxsum
