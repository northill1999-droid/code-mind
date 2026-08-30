class Solution:
    def decimalToBinary(self, n: int) -> str:
        lst = []
        while True:
            lst.append(n % 2)
            if n // 2 == 0:
                return "".join(map(str, lst[::-1]))
            n = n // 2


if __name__ == "__main__":
    sol = Solution()
    print(sol.decimalToBinary(6))
    print(sol.decimalToBinary(2))
    # print(sol.decimalToBinary(0))
    print(sol.decimalToBinary(10))
    