# https://leetcode.cn/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        cnt = 0
        def fcn1(n1):
            nonlocal cnt

            if n1 > n:
                return
            if n1 == n:
                cnt += 1
                return

            fcn1(n1 + 1)

            fcn1(n1 + 2)

        fcn1(0)

        return cnt


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))
    print(sol.climbStairs(3))