from itertools import combinations
import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        subset = []

        def create_subsets(i):
            # Search complete
            if i == len(nums):
                # Copy the current subset to result
                power_set.append(subset[:])
                return

            subset.append(nums[i])
            create_subsets(i+1)

            subset.pop()
            create_subsets(i+1)

        create_subsets(0)

        return power_set

        
