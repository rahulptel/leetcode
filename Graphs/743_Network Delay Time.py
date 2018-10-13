class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        cost = [101] * N
        cost[K-1] = 0
        visited = set()
        not_visited = set(range(1, N+1))

        while len(list(visited)) != N:
            # Select the current node
            remaining = list(not_visited.difference(visited))
            remaining = [(vertex, cost[vertex-1]) for vertex in remaining]
            remaining.sort(key=lambda tup: tup[1])
            selected_vertex = remaining[0][0]

            # Update cost through the current node
            relevant_time = [
                time for time in times if time[0] == selected_vertex]
            # print(relevant_time)
            for time in relevant_time:
                if cost[time[1]-1] > cost[time[0]-1] + time[2]:
                    cost[time[1]-1] = cost[time[0]-1] + time[2]

            # print(selected_vertex)
            # Remove current node from not_visited and add to visited
            visited = visited.union(set([selected_vertex]))
            not_visited.remove(selected_vertex)

        return -1 if 101 in cost else max(cost)
