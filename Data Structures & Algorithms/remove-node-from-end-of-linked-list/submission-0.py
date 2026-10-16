# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        trail = dummy
        lead = head
        for i in range(n-1):
            lead = lead.next

        while lead.next is not None:
            lead = lead.next
            trail = trail.next

        to_delete = trail.next
        trail.next = to_delete.next

        return dummy.next
        