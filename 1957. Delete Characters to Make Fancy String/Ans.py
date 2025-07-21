class Solution(object):
    def makeFancyString(self, s):

        stack = [s[0]]
        q = 1
        for i in s:
            if i == stack[-1]:
                stack.append(i)
                print(q)
                if q == 2:
                    stack.pop()
                    q = 0
                else :
                    q += 1
            
            else :
                stack.append(i)
                stack.pop()
                stack.append(i) 

        return stack 

s = "aaabaaaa"
solution = Solution()
result = solution.makeFancyString(s)
print(result)