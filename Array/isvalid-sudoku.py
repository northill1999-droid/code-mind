# https://leetcode.cn/problems/valid-sudoku/
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        column = len(board[0])

        def check(x, y):
            for c in range(column):
                if y != c and board[x][y] == board[x][c]:
                    return False

            for r in range(row):
                if x != r and board[x][y] == board[r][y]:
                    return False

            beg_x = (x // 3) * 3
            beg_y = (y // 3) * 3
            for i in range(beg_x, beg_x+3):
                for j in range(beg_y, beg_y+3):
                    if (x != i or y != j) and board[x][y] == board[i][j]:
                        return False

            return True
                    
        for i in range(row):
            for j in range(column):
                if board[i][j] != "." and not check(i, j):
                    return False

        return True


# if __name__ == "__main__":
#     sol = Solution()
#     # print(sol.isValidSudoku())