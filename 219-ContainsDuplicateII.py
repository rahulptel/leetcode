class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i, n in enumerate(nums):
            if i > k:
                seen.remove(nums[i-k-1])

            if n in seen:
                return True

            seen.add(n)

        return False
        
