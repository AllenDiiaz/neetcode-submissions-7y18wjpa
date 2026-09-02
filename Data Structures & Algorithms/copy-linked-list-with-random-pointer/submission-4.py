"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # next:    [3] → [7] → [4] → [5] → None 
        # index:    0     1     2     3
        # random:  [3].random = None
        #          [7].random = [5]
        #          [4].random = [3]
        #          [5].random = [7]

        old_to_new = {None: None}

        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = old_to_new[cur]
            copy.next = old_to_new[cur.next]
            copy.random = old_to_new[cur.random]
            cur = cur.next

        return old_to_new[head]




        