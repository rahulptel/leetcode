class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        partners = {}
        for i, n in enumerate(nums):
            partner = target - n
            if partner in partners:
                return [i, partners[partner]]
            else:
                partners[n] = i
