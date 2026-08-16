# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # virtual ─→ None
        #   ↑
        #  tail

        # [1a] ─→ [2] ─→ [4] ─→ None
        #   ↑
        # list1

        # [1b] ─→ [3] ─→ [5] ─→ None
        #   ↑
        # list2 

        virtual = ListNode()
        tail = virtual

        while list1 and list2:

            if list1.val <= list2.val:
                tail.next = list1      
                # virtual ─→ [1a] ─→ [2] ─→ [4] ─→ None
                #   ↑          ↑
                #  tail      list1
                list1 = list1.next
                # virtual ─→ [1a] ─→ [2] ─→ [4] ─→ None
                #   ↑                 ↑
                #  tail             list1
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            # virtual ─→ [1a] ─→ [2] ─→ [4] ─→ None
            #             ↑       ↑
            #            tail   list1

        tail.next = list1 if list1 else list2

        return virtual.next









        