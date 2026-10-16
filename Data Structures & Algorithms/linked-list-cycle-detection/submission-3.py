# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#class Solution:
#    def hasCycle(self, head: Optional[ListNode]) -> bool:
#        slow, fast = head, head
#        while fast is not None:
#            if fast.next is None:
#                return False
#            fast = fast.next
#            if fast.next is  None:
#                return False
#            fast = fast.next    
#            slow = slow.next

#            if slow == fast:
#                return True
        
#        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next
            fast = fast.next    
            slow = slow.next

            if slow == fast:
                return True
        
        return False
            