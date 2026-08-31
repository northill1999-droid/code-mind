# https://leetcode.cn/problems/duplicate-zeros/

from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> List:
        last_index = 0

        count = 0
        for i in arr:
            if i != 0:
                count += 1
            else:
                count += 2
                # print(f"zero occurent!")

            # print(f"len = {len(arr)}, count = {count}")

            if count >= len(arr):
                break

            last_index += 1

        print(f"last_ind = {last_index}")

        slow = len(arr) - 1
        if count >= len(arr) + 1:
            arr[slow] = 0
            slow -= 1
            last_index -= 1

        while last_index >= 0:
            # print(f"{last_index}, arr[] = {arr[last_index]}")

            if arr[last_index] != 0:
                arr[slow] = arr[last_index]
                slow -= 1
            else:
                arr[slow] = 0
                slow -= 1
                if slow > 0:
                    arr[slow] = 0
                    slow -= 1
                
            last_index -= 1
            

        return arr
                


if __name__ == "__main__":
    sol = Solution()
    # print(sol.duplicateZeros([1,0,2,3,0,4,5,0]))  # 1 0 0 2 3 0 0 4
    # print(sol.duplicateZeros([1,2,3]))
    # print(sol.duplicateZeros([0,1,7,6,0,2,0,7]))
    print(sol.duplicateZeros([8,4,5,0,0,0,0,7]))