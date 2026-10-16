# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        # find middle
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next
            fast = fast.next    
            slow = slow.next

        # split
        head_scnd = slow.next
        slow.next = None
        
        # reverse second half
        tmp_prev = None
        while head_scnd is not None:
            tmp_next = head_scnd.next
            head_scnd.next = tmp_prev
            tmp_prev = head_scnd
            head_scnd = tmp_next

        # zip both
        first_half = head
        second_half = tmp_prev
        
        while first_half is not None and second_half is not None:
            # save next element of both lists
            first_next = first_half.next
            second_next = second_half.next
            # reassign it
            first_half.next = second_half
            # point second half node to original first half next
            second_half.next = first_next
            # progress both heads
            first_half = first_next
            second_half = second_next





        

        
                


        