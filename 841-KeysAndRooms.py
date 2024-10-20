class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if len(rooms) == 1:
            return True

        visited = set({0})
        next_visit = set(rooms[0]).difference({0})

        while len(next_visit) > 0:
            curr = next_visit.pop()
            visited = visited.union({curr})
            for room in rooms[curr]:
                if room not in visited and room not in next_visit:
                    next_visit = next_visit.union({room})

        return True if len(rooms) == len(visited) else False
