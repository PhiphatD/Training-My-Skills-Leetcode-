class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in hash :
                if stack and stack[-1] == hash[i] :
                    stack.pop()
                else :
                    return False
            else :
                stack.append(i)
        if stack:
            return False
        return True
 
s = "("
solution = Solution()
result = solution.isValid(s)
print(result)