# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            prev, next=None, head.next
            while next is not None:
                head.next = prev
                prev = head
                head = next
                next = head.next
            
            head.next = prev

        return head

        
