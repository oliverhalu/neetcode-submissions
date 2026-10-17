# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result_head = result
        carry = 0
        while l1 is not None or l2 is not None or carry == 1:
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            sum = l1_val + l2_val + carry
            if sum >= 10:
                sum -= 10
                carry = 1
            else: 
                carry = 0
            
            result.val = sum

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            
            if l1 is not None or l2 is not None or carry == 1:
                result.next = ListNode()
                result = result.next
        
        return result_head
            
            
        