class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left, right = 1, sum(ribbons) // k + 1
        x = 0        
        while left <= right:
            
            mid = int((left + right)/2)            
            cuts = 0
            for r in ribbons:
                cuts += r // mid
                
            can_break = cuts >= k
            if can_break:
                left = mid + 1
                x = mid                
            else:
                right = mid - 1

        return x
        
