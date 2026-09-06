class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for i in s:
            count[i] = count.get(i, 0) + 1

        length = 0
        odd_flag = 0
        final = 0
        for c in count.values():
            length = c // 2 * 2
            if c % 2 == 1:
                odd_flag = 1
            final += length

        return final + odd_flag

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("abba"))
