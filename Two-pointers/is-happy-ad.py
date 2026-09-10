# https://leetcode.cn/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit ** 2
                n = n // 10
            return total_sum

        slow = n
        fast = n

        while True:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            # print(f"slow: {slow}, fast: {fast}")

            if fast == 1:
                return True
            if fast == slow:
                return False
            
        # return


if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))  # true
    print(sol.isHappy(2))  # false