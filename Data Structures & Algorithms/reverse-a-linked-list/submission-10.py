# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # None    0 -> 1 -> 2 -> 3 -> None

        # prev  cur

        # None <- 0

        #        prev

        # None <- 0 <- 1 <- 2 <- 3

        prev = None
        cur = head

        while cur:

            temp = cur.next   # temp: 1 -> 2 -> 3 -> None
            cur.next = prev   # None <- 0
            prev = cur        #        prev
            cur = temp        #              1 -> 2 -> 3 -> None
                              #             cur

                              # temp: 2 -> 3 -> None
                              # None <- 0 <- 1
                              #             prev
                              #                   2 -> 3 -> None
                              #                  cur

                              # temp: 3 -> None
                              # None <- 0 <- 1 <- 2
                              #                  prev
                              #                        3 -> None
                              #                       cur

                              # temp: None
                              # None <- 0 <- 1 <- 2 <- 3
                              #                       prev
                              #                             None
                              #                              cur
        return prev



        