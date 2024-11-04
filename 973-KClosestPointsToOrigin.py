import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_points = [[p[0]**2 + p[1]**2, p[0], p[1]] for p in points]
        heapq.heapify(dist_points)                
        result = []
        for _ in range(k):
            r = heapq.heappop(dist_points)
            result.append([r[1], r[2]])
        
        return result
        # Quickselect
        # ------------------------------
        # low, high = 0, len(points) - 1        
        # dists = {tuple(point): point[0]**2+point[1]**2 for point in points}
        # pivot_idx = 0
        # print(dists)
        # while pivot_idx < k:
        #     print("STart", points)
        #     pivot_dst = dists[tuple(points[high])]
        #     p = low
        #     for i in range(low, high):            
        #         if dists[tuple(points[i])] <= pivot_dst:
        #             points[p], points[i] = points[i], points[p]
        #             p += 1        
        #     if p < len(points):                                            
        #         points[p], points[high] = points[high], points[p]

        #     print("p", p)
        #     if p <= k:
        #         pivot_idx += p + 1 - low
        #         low = p + 1            
        #     else:
        #         high = p - 1
        #     print("low: ", low, " high: ", high, "pivot :", pivot_idx)

        #     print("End", points)

        # return points[:k]
            
            




        
