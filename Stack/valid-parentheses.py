class Solution:
    def isValid(self, s: str) -> bool:

        dic = {"(": ")", "{": "}", "[": "]"}

        lst = [i for i in s]
        lst1 = []
        for i in lst[-1::-1]:
            if i in dic.keys():
                if lst1 and dic[i] == lst1[-1]:
                    lst1.pop()
                    continue
                return False
            lst1.append(i)
            # print(f"lst1 push {i}", end = ' ')
            # return False
        if lst1:
            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    # print(sol.isValid("()[]{}"))
    print(sol.isValid("]"))
    # print(sol.isValid("([)]"))