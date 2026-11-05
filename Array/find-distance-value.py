# 链接：https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/solutions/168350/liang-ge-shu-zu-jian-de-ju-chi-zhi-by-leetcode-sol/ 

from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt = 0
        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                cnt += 1
        return cnt


