from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = deque()
        water = 0
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        while left < right:
            if height[left] <= height[right]:                
                diff = max_left - height[left]
                if diff > 0:
                    water += diff
                max_left = max(height[left], max_left)
                left += 1
            else:
                diff = max_right - height[right]
                if diff > 0:
                    water += diff
                max_right = max(height[right], max_right)
                right -= 1

        return water
