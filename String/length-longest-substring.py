# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0

        s1 = ""
        length = 0

        # lst = []

        # for i in range(len(s)):
        while right <= len(s) - 1:

            if s[right] in s1:
                # length = right - left
                if (right - left) > length:
                    length = right - left

                # lst.append(right - left)

                s1 = ""

                for j in range(left, right):
                    if s[j] == s[right]:
                        left = j + 1
                        right = j + 1
                        # print(f"\nleft: {left}, right: {right}\n")
                        break
                # continue

            s1 += s[right]
            if len(s1) > length:
                length = len(s1)

            right += 1

            # print(s1, end=" ")
            

        # print(lst)

        return length


if __name__ == "__main__":
    sol = Solution()
    # print(sol.lengthOfLongestSubstring("abcabcbb"))  # 3
    # print(sol.lengthOfLongestSubstring("bbbb"))  # 1
    # print(sol.lengthOfLongestSubstring("pwwkew"))  # 3
    # print(sol.lengthOfLongestSubstring("S"))  # 0
    print(sol.lengthOfLongestSubstring("mq"))