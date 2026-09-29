# https://leetcode.cn/problems/merge-k-sorted-lists/solutions/219756/he-bing-kge-pai-xu-lian-biao-by-leetcode-solutio-2/

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, a: ListNode, b: ListNode) -> ListNode:
        if not a or not b:
            return a or b

        head = ListNode()
        tail = head

        aPtr, bPtr = a, b
        while aPtr and bPtr:
            if aPtr.val < bPtr.val:
                tail.next = aPtr
                aPtr = aPtr.next
            else:
                tail.next = bPtr
                bPtr = bPtr.next
            tail = tail.next

        tail.next = aPtr if aPtr else bPtr
        return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = None
        for lst in lists:
            ans = self.mergeTwoLists(ans, lst)

        return ans
    