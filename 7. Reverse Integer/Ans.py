class Solution(object):
    def reverse(self, x):

        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1]) * sign
        if -2**31 <= rev <= 2**31-1:
            return rev
        else:
            return 0

        
x = -2147483647
solution = Solution()
result = solution.reverse(x)
print(result)