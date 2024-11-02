class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = int((low + high)/2)
            # Peak in left subarray
            if nums[mid] > nums[mid+1]:
                high = mid
            # Peak in right subarray
            else:
                low = mid + 1

        return low
