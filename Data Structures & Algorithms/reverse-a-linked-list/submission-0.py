# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp_prev = None
        while head is not None:
            tmp_next = head.next
            head.next = tmp_prev
            tmp_prev = head
            head = tmp_next


        return tmp_prev
