from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Find the counts of each element
        cnts = {}
        for n in nums:
            cnts[n] = 1 + cnts.get(n, 0)

        h = []
        for n, c in cnts.items():
            heappush(h, (c, n))
            if len(h) > k:
                heappop(h)

        r = []
        while k:
            r.append(heappop(h)[1])
            k -= 1

        return r
