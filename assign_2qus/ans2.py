class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        import math
        if str1 + str2 != str2 + str1:
            return ""
        d = math.gcd(len(str1), len(str2))
        return str1[:d]
        
str1 = "ABABAB"
str2 = "ABAB"
solution = Solution()
result = solution.gcdOfStrings(str1, str2)
print(result)  # Output: ""