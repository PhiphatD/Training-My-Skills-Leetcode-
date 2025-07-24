class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        qty = 0
        max_length = 0
        i = len(s)-1 
        while i >= 0 and s[i] != " ":
            qty += 1
            i -= 1
        while i >= 0 and s[i] == " ":
            if qty > max_length :
                max_length = qty 
                qty = 0
            i -= 1
        return max_length

    
    
    
s = "   fly me   to   the moon  "
solution = Solution()
reusult = solution.lengthOfLastWord(s)
print(reusult)