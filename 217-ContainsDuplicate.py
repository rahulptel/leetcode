class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for n in nums:
            if n in counter:
                return True
            else:
                counter[n] = 1

        return False
