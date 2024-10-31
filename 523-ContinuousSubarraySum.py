class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Init hashmap to store remainders-index mapping
        remainder_idx_map = {0: -1}
        total = 0

        # Compute remainder for prefix_i, i=0...len(nums)
        for i, v in enumerate(nums):
            total += v
            remainder = total % k

            # Check if remainder already present in hashmap
            if remainder in remainder_idx_map:
                # Check if the sub-array is of size 2
                if i - remainder_idx_map[remainder] > 1:
                    return True
            else:
                remainder_idx_map[remainder] = i 

        return False
                


