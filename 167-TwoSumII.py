class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers) - 1 
        i, j = 0, size
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i+1, j+1]
            elif total < target:
                i += 1
            else:
                j -= 1
        
