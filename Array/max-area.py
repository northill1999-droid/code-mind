from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # area = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         width = j - i
        #         min_height = min(height[i], height[j])
        #         area1 = width * min_height
        #         if area1 > area:
        #             area = area1

        areas = []
        left = 0
        right = len(height) - 1
        while left < right:
            areas.append((right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max(areas)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
    print(sol.maxArea([1,1]))
