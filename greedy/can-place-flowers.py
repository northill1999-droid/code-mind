from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        initial = sum(flowerbed)
        for i, plant in enumerate(flowerbed):
            if i > 1 and i < len(flowerbed) - 1:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and plant == 0:
                    flowerbed[i] = 1

        if len(flowerbed) >= 2:
            if flowerbed[1] == 0 and flowerbed[0] == 0:
                flowerbed[0] = 1
            if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                flowerbed[-1] = 1
        else:
            flowerbed[0] = 1
            
        if sum(flowerbed) - initial >= n:
            return True
        return False

if __name__ == "__main__":
    sol = Solution()
    # print(sol.canPlaceFlowers([1,0,0,0,1], 1))  # true
    # print(sol.canPlaceFlowers([1,0,0,0,1], 2))  # false

    print(sol.canPlaceFlowers([0], 1))  # false