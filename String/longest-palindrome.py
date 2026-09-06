# https://leetcode.cn/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        start = 0
        max_len = 1

        for i in range(n):
            for j in range(i + max_len, n):
                if self.is_palindrome(s, i, j):
                    start = i
                    max_len = j - i + 1

        return s[start:start + max_len]


    def is_palindrome(self, s: str, left: int, right: int) -> bool:

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))
    print(sol.longestPalindrome("cbbd"))