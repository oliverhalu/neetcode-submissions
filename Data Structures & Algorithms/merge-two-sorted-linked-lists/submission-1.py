# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        dummy = ListNode()
        result = dummy
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                saved_list1 = list1
                list1 = list1.next
                result.next = saved_list1
                result = result.next
            else:
                saved_list2 = list2
                list2 = list2.next
                result.next = saved_list2
                result = result.next

        # handle remaining nodes
        if list1 is None:
            result.next = list2
        else:
            result.next = list1
        
        return dummy.next
        