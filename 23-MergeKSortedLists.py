import heapq

class HeapNode:
    def __init__(self, node):
        self.node = node
        
    def __lt__(self, heap_node):
        return self.node.val < heap_node.node.val

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = None
        curr = None
        for ll_head in lists:
            if ll_head is not None:
                heapq.heappush(heap, HeapNode(ll_head))

        while len(heap):
            heap_node = heapq.heappop(heap)
            ll_node = heap_node.node
            
            if ll_node.next is not None:
                heapq.heappush(heap, HeapNode(ll_node.next))

            if head is None:
                head = ll_node
                curr = ll_node
            else:
                curr.next = ll_node
                curr = curr.next
        
        return head
                

        
