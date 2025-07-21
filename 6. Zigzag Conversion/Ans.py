class Solution(object):
    def convert(self, s, numRows):
        print(s)
        print(range(numRows))
        
        if s == 1 :  #ในกรณีที่ สตริงมีตัวเดียว
            return s 
        convert_list = [[] for _ in range(numRows)]  #สร้างลิสแบบตาม numRows
        
        i = 0 
        n = len(s)
        
        while i < n:
            for down in range(numRows):
                if i < n :
                    convert_list[down].append(s[i])
                    i+=1
            for up in range(numRows -2,0,-1):
                if i < n :
                    convert_list[up].append(s[i])
                    i+=1 
        ans = ''
        for i in convert_list:
            ans +=''.join(i)
        return ans










s = "PAYPALISHIRING" 
numRows = 3
solution = Solution()
result = solution.convert(s, numRows)
print(result)