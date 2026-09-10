# https://leetcode.cn/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:

        rest = 0
        res = 0
        found = []

        cnt = 0

        while n > 0: 

            while n > 0:
                rest = n % 10
                print(f"rest = {rest}", end=" ")
                res += rest ** 2
                n = n // 10

            if res == 1:
                return True
            
            elif res in found:
                return False

            else:
                found.append(res)
                n = res
                res = 0

                cnt += 1
                # if cnt >= 5:
                #     break
                print("\n" + f"n = {n}")
                
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))  # true
    print(sol.isHappy(2))  # false