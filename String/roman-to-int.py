# https://leetcode.cn/problems/integer-to-roman/description/?envType=problem-list-v2&envId=hash-table

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        ans = 0

        n = len(s)
        slow = 0

        while slow < n:
            if slow + 1 < n and s[slow:slow+2] in dic:
                ans += dic[s[slow:slow+2]]
                slow += 2
                
            else:
                ans += dic[s[slow]]
                slow += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))
    print(sol.romanToInt("LVIII"))
