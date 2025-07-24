class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.strip()
        word = s.split()
        return len(word[-1])
    
    
s = "Today is a nice day"
solution = Solution()
reusult = solution.lengthOfLastWord(s)
print(reusult)