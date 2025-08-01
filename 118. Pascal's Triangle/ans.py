class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(2, numRows + 1):
            res.append([1] + [res[-1][j] + res[-1][j + 1] for j in range(i - 2)] + [1])
        return res
    
    
    
    
numRows = 5
solution = Solution()
result = solution.generate(numRows)
print(result)