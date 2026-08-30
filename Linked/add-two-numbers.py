from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # to be continue
        return None


def list_to_linked(lst):
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
    print(sol.addTwoNumbers(list_to_linked([2,4,3]), list_to_linked([5,6,4])))
