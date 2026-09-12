# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


def lst_to_node(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    cur = head

    for i in lst[1:]:
        cur.next = ListNode(i)
        cur = cur.next

    return head


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeNthFromEnd(lst_to_node([1,2,3,4,5]), 2))