# https://leetcode.cn/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        # horizontal scanning
        result = 0
        ind = 0
        a = strs[0]
        for i in strs[1::]:
            temp = self.comparison(a, i)
            if temp < result:
                result = temp
                continue
            result = temp

        if result == 0:
            return "The common prefix does not exist."
        return a[:result:]
            
    @staticmethod
    def comparison(a, b):
        lst1 = [i for i in a]
        lst2 = [i for i in b]
        ind = 0
        result = 0
        while True:
            if lst1[ind] == lst2[ind]:
                result += 1
            else:
                return result

            ind += 1
            if ind >= min(len(lst1), len(lst2)):
                return result

if __name__ == "__main__":
    a = Solution()
    result = a.longestCommonPrefix(["flower","flow","flight"])
    result1 = a.longestCommonPrefix(["dog","racecar","car"])
    print(result)
    print(result1)
        
                

