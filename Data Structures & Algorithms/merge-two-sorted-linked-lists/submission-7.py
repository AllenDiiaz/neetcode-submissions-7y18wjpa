# Definition for singly-linked list.


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        vir = ListNode()
        tail = vir

        while list1 and list2:

            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return vir.next
                


# virtual ─→ None
#   ↑
#  tail

# [1a] ─→ [2] ─→ [4] ─→ None
#   ↑
# list1

# [1b] ─→ [3] ─→ [5] ─→ None
#   ↑
# list2 


# virtual ─→ [1a] ─→ [2] ─→ [4] ─→ None
#              ↑      ↑
#            tail.  list1

# virtual ─→ [1a] ─→ [1b] ─→ [3] ─→ [5] ─→ None
#                     ↑       ↑
#                    tail.   list2

# virtual ─→ [1a] ─→ [1b] ─→ [3] ─→ [5] ─→ None
#                     ↑       ↑
#                    tail.   list2

# virtual ─→ [1a] ─→ [1b] ─→ [2] ─→ [4] ─→ None
#                             ↑      ↑
#                           tail.   list1

# virtual ─→ [1a] ─→ [1b] ─→ [2] ─→ [3] ─→ [5] ─→ None
#                                    ↑       ↑
#                                   tail.   list2

# virtual ─→ [1a] ─→ [1b] ─→ [2] ─→ [3] ─→ [4] ─→ None
#                                           ↑       ↑
#                                         tail.   list1

# virtual ─→ [1a] ─→ [1b] ─→ [2] ─→ [3] ─→ [4] ─→ [5] ─→ None
#                                                  ↑       ↑
#                                                tail.   list2
