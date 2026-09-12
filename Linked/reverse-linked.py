# https://leetcode.cn/problems/UHnkqh/

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        pre = None
        cur = head
        while cur:
            nxt = cur.next

            cur.next = pre
            pre = cur

            cur = nxt

        return pre

def lst_to_linked(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    cur = head

    for i in lst[1:]:
        cur.next = ListNode(i)
        cur = cur.next

    return head


def linked_to_lst(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next

    return res

if __name__ == "__main__":
    sol = Solution()
    print(linked_to_lst(sol.reverseList(lst_to_linked([1,2,3,4,5]))))