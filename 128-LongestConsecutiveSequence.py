class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_seq = 0

        for n in nums:
            # start 
            if n-1 not in nums:
                seq = 1
                s = n
                while True:
                    if s + 1 in nums:
                        seq += 1
                        s = s + 1
                    else:
                        break
                if seq > longest_seq:
                    longest_seq = seq

        return longest_seq
