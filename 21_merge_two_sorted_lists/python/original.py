from typing import Optional
from ...utils.listnode import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        prehead = ListNode(-1)
        curr = prehead
        c1, c2 = list1, list2
        while c1 and c2:
            if c1.val <= c2.val:
                curr.next = c1
                c1 = c1.next
            else:
                curr.next = c2
                c2 = c2.next
            curr = curr.next

        curr.next = c2 if c1 is None else c1
        return prehead.next
