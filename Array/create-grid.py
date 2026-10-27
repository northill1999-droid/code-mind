# https://leetcode.cn/problems/create-grid-with-exactly-one-path/solutions/3986086/gou-zao-ti-jian-dan-zuo-fa-pythonjavacgo-jtvi/

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ['.' * n] + ['#' * (n - 1) + '.'] * (m - 1)


