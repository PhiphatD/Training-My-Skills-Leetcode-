class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """ 
        
        return int(pow(x, 0.5))
    

x = 0
solution = Solution()
result = solution.mySqrt(x)
print(result)