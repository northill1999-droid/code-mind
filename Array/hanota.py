# https://leetcode.cn/problems/hanota-lcci/
from typing import List

class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> List:
        n = len(A)
        self.move(n, A, B, C)
        return C

    def move(self, n, A: List[int], B: List[int], C: List[int]):
        if n == 1:
            C.append(A[-1])
            A.pop()
            return

        else:
            self.move(n-1, A, C, B)
            C.append(A[-1])
            A.pop()
            self.move(n-1, B, A, C)
            


if __name__ == "__main__":
    sol = Solution()
    print(sol.hanota([2, 1, 0], [], []))
    print(sol.hanota([1, 0], [], []))
