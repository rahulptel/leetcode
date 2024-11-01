class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) == 1: 
            return [0]

        buildings = [len(heights) - 1]
        max_height = heights[len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > max_height:
                max_height = heights[i]
                buildings.append(i) 

        buildings.reverse()
        return buildings
        
        
