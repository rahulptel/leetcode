class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_seq = 0

        for num in nums:
            # start 
            if num-1 not in nums:
                seqlen = 1
                curr_num = num
                while curr_num + 1 in nums:
                    curr_num += 1
                    seqlen += 1
                    
                longest_seq = max(longest_seq, seqlen)

        return longest_seq
