class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        x = str(x)
        for i in range(len(x)):
            pal1 = solution.expend(x,i,i)
            pal2 = solution.expend(x,i,i+1)
            if len(pal1) == len(x):
                return True
            if len(pal2) == len(x): 
                return True
        return  False   
    def expend(self, x, left, right):
        while left >= 0 and right < len(x) and x[left] == x[right]:
            left -= 1
            right += 1 
        return x[left + 1:right] 
        
x = 121111111111111111111111111111111111111111111111111111111111111111112211111111111111111111111111111111111111
solution = Solution()
result = solution.isPalindrome(x)
print(result)