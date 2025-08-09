class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0 :
            return (n & (n - 1)) == 0
        return False
    
solution = Solution()
result = solution.isPowerOfTwo(0)
print(result)