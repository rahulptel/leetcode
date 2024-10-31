import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # Add element to heap
        for n in nums:
            heapq.heappush(heap, n)
            # Pop the root if the heap size exceeds k            
            if len(heap) > k:
                heapq.heappop(heap)

        # Return the head of the heap
        return heapq.heappop(heap)
        
