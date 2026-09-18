# https://leetcode.cn/problems/teemo-attacking/?envType=problem-list-v2&envId=array

class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        ans = 0
        expired = 0

        for i in range(len(timeSeries)):
            if timeSeries[i] > expired:
                ans += duration
            else:
                ans += timeSeries[i] + duration - expired

            expired = timeSeries[i] + duration

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPoisonedDuration([1,4], 2))  # 4
    print(sol.findPoisonedDuration([1,2], 2))  # 3
    