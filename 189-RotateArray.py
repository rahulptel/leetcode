import copy
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if k > size:
            k = k % size

        nums_copy = nums[size - k:]        
        for i in range(size-k-1, -1, -1):
            nums[i+k] = nums[i]

        nums[:k] = nums_copy
