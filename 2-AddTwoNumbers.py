# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        carry = 0
        c1, c2 = l1, l2
        sentinal = ListNode()
        c3 = sentinal
        while c1 or c2:
            op1 = 0
            if c1 is not None:
                op1 += c1.val

            if c2 is not None:
                op1 += c2.val

            addition = op1 + carry            
            c3.next = ListNode(addition % 10)
            carry = addition // 10
            

            if c1 is not None:
                c1 = c1.next
            if c2 is not None:
                c2 = c2.next
            c3 = c3.next

        if carry > 0:
            c3.next = ListNode(carry)

        return sentinal.next

            

        
