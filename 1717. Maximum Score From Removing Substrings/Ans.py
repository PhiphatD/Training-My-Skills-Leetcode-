class Solution:
    def maximumGain(self, s, x, y):
        res = 0
        for q,t in sorted(((x,'ab'),(y,'ba')))[::-1]:
            stack = []
            for ch in s:
                if stack and stack[-1]+ch == t:
                    res += q
                    stack.pop()
                else:
                    stack.append(ch)
        
            s = stack

        return res
    
    
s = "aabbaaxybbaabb"
x = 5
y = 4
solution = Solution()
result = solution.maximumGain(s,x,y)
print(result)