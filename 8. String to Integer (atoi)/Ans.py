class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        sign = 1
        result = ""
        i = 0
        if i < len(s) and s[i] in '+-' :
            sign = -1 if s[i] =='-' else 1
            i += 1 
            
        while i < len(s) and s[i].isdigit():
            result += s[i]
            i += 1
            
        if result == '':
            return 0
        result = int(result)* sign

        
        if result < -2**31 : 
            return -2**31
        if result > 2**31-1 : 
            return  2**31-1
        return result

x = "   -042"
solution = Solution()
result = solution.myAtoi(x)
print(result)





