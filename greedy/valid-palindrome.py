class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(lst):
            for i in range(len(lst) // 2):
                if lst[i] == lst[len(lst) - (i + 1)]:
                    continue
                return False
            return True

        lst = [i for i in s]
        # valid = 0
        for i in range(len(lst) // 2):
            if lst[i] == lst[len(lst) - (i + 1)]:
                continue
            else:
                lst1 = lst[:]
                del lst1[len(lst) - (i + 1)]
                del lst[i]
                # print(f"i = {i}, lst = {lst}, lst1 = {lst1}")
                return palindrome(lst) if palindrome(lst) else palindrome(lst1)
                
        print("END:", end=' ')
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.validPalindrome("bba"))  # false