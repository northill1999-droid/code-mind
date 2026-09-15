# class Solution:
#     def gcdOfOddEvenSums(self, n: int) -> int:
#         def sum_odd(n):
#             odd = 0
#             i = 0
#             while n > 0:
#                 i += 1
#                 if i % 2 != 0:
#                     odd += i
#                     n -= 1
            
#             return odd

#         def sum_even(n):
#             even = 0
#             i = 0
#             while n > 0:
#                 i += 1
#                 if i % 2 == 0:
#                     even += i
#                     n -= 1
#             return even

#         def gcd(a, b):
#             while b != 0:
#                 a, b = b, a % b
#             return a

#         even = sum_even(n)
#         odd = sum_odd(n)
#         print(f"even = {even}, odd = {odd}")

#         return gcd(sum_odd(n), sum_even(n))

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(x: int, y: int) -> int:
            return x if y == 0 else gcd(y, x % y)
        return gcd(n * n, n * (n + 1))
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.gcdOfOddEvenSums(4))  # 4
    print(sol.gcdOfOddEvenSums(5))  # 5