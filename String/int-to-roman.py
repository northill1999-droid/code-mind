# https://leetcode.cn/problems/integer-to-roman/description/?envType=problem-list-v2&envId=hash-table

class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        ans = ""
        while num > 0:
            for k, v in dic.items():
                most = num // v

                for _ in range(most):
                    ans += k
                    num -= v

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(3749))
    print(sol.intToRoman(58))