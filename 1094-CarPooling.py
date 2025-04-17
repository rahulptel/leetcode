class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ticks = []
        for trip in trips:
            # Add passengers
            ticks.append([trip[1], trip[0]])
            # Remvoe passengers
            ticks.append([trip[2], -trip[0]])

        ticks.sort()
        
        passengers = 0
        for _, c in ticks:
            passengers += c
            if passengers > capacity:
                return False

        return True
