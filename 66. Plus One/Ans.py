class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        num_int = ""
        for i in digits :
            num_int += str(i) 
        
        plusone = int(num_int) + 1
        new_digit  = []
        for i in str(plusone) :
            new_digit.append(int(i))
        
        return new_digit
    
    
digits = [0]  
solution = Solution()
result = solution.plusOne(digits)
print(result)