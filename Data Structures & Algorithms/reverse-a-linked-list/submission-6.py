# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Now: [0]→[1]→[2]→[3]→ None
        #      cur
        # Goal: None ←[0]←[1]←[2]←[3]

        prev = None
        cur = head

        while cur:

            # 記住 next ptr
            temp = cur.next
            # 反轉 ptr.          None ←[0] [1]→[2]→[3]→ None
            #                   prev  cur
            cur.next = prev
            # 把 cur 變成 prev   None ←[0] [1]→[2]→[3]→ None
            #                         prev
            prev = cur
            # 走到下一個 node     None ←[0] [1]→[2]→[3]→ None
            #                         prev cur
            cur = temp

        return prev
        