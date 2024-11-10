class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        
        max_area = 0
        i, j = 0, size - 1        
        while i < j:
            top = min(height[i], height[j])
            width = j - i                
            area = (top * width)
            # print(i, j, top, width, area)

            if area > max_area:
                max_area = area

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return max_area
