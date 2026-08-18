# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 步驟 1:快慢指針找中點,切成兩半
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # 步驟 2:反轉後半
        prev = None
        cur = second

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        second = prev

        # 步驟 3:交錯合併
        first = head
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2







        