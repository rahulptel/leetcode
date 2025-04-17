class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = 0
        leftSum = [0]
        for n in nums[:-1]:
            sum_ += n
            leftSum.append(sum_)

        sum_ = 0
        rightSum = [0]
        for n in nums[::-1][:-1]:
            sum_ += n
            rightSum.insert(0, sum_)
        
        for i in range(len(nums)):
            if leftSum[i] == rightSum[i]:
                return i

        return -1

        
