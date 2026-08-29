from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        lst1 = []
        lst2 = []
        lst3 = []

        for i in bills:
            if i == 5:
                lst1.append(i)
            elif i == 10:
                lst2.append(i)
            else:
                lst3.append(i)

            need_recall = i - 5
            while lst1 and need_recall > 0:
                while lst2 and need_recall >= 10:
                    need_recall -= lst2.pop(0)
                need_recall -= lst1.pop(0)

            # print(need_recall)
            if need_recall != 0:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.lemonadeChange([5,5,5,10,20])) 
    print(sol.lemonadeChange([5,5,10,10,20]))
    