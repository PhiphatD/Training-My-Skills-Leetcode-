class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_stmbol = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        for i in range(len(s)): 
            if i + 1 < len(s) and char_stmbol[s[i]] < char_stmbol[s[i+1]]:
                sum -= char_stmbol[s[i]]
            else:
                sum += char_stmbol[s[i]]
        return sum
    
s = "MCMXCIV"
solution = Solution()
result = solution.romanToInt(s)
print(result)

#Check