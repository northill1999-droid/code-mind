# https://leetcode.cn/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ind = -1
        found = 1
        while True:
            # print(digits)

            if found == 0 and digits[ind] < 10:
                return digits

            if digits[ind] >= 10:
                ind -= 1

                if abs(ind) > len(digits):
                    digits = [1] + digits
                    digits[1] -= 10
                    return digits

                digits[ind] += 1
                digits[ind+1] -= 10
                
                found = 0
                continue

            if found == 1:
                digits[ind] = digits[ind] + 1
                found = 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))

    # print(sol.plusOne([9]))

    # print(sol.plusOne([8, 9, 9, 9]))
            