# https://leetcode.cn/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:  # my ASCLL to Integer
        s = s.strip()
        if not s:
            return 0

        # sign = 1 if s[0] == '+' else '-'
        sign = 1
        index = 0
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1

        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        nums = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        while index < len(s) and s[index].isdigit():
            # if result == 0 and int(s[index]) == 0:
            #     index += 1
            #     continue

            dight = nums[s[index]]

            if result > INT_MAX // 10 or (result == INT_MAX // 10 and dight > 7):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + dight
            index += 1

        return sign * result

if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi(""))
