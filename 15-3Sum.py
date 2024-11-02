class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]            
            return []

        indices = []
        nums.sort()
        for i, n1 in enumerate(nums):
            if i > len(nums) - 3:
                break
            if i > 0 and n1 == nums[i-1]:
                continue

            low, high = i+1, len(nums) - 1
            while low < high:                
                sum_ = n1 + nums[low] + nums[high]                    
                if sum_ < 0:                    
                    low += 1                    
                elif sum_ > 0:                    
                    high -= 1                    
                else:
                    indices.append([n1, nums[low], nums[high]])
                    low += 1
                    while low < len(nums) and nums[low] == nums[low-1]:
                        low += 1
                                                                
        return indices                
