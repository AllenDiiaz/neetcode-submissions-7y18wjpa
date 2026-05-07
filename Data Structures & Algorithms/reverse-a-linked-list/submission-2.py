# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # prev (None)  0   next -> 1 next -> 2 next -> 3 next -> None
        #            [curr]

        # [1：初始化觀測者 prev 和 curr]
        prev = None
        curr = head
        # [2：寫一個 while 迴圈，只要 curr 還沒走到盡頭]
        while curr:
            # [3：執行動作 B (備份未來 nxt)]
            nxt = curr.next
            # [4：執行動作 A (轉向過去)]
            curr.next = prev
            # [5：執行動作 C (時間線推進)]
            # 先讓 prev 走到現在的 curr 位置，再讓 curr 走到剛剛備份好的 nxt 位置
            prev = curr   # 過去跟上現在
            curr = nxt    # 現在走向未來

        return prev




        