class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        if len(nums) == 1:
            return 1

        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                if i != j:
                    nums[i] = nums[j]

            j += 1

        i += 1
        return i

        
        
