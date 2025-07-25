class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if all(n < 0 for n in nums):
            return max(nums)
        
        unique = set(nums)
        return sum(n for n in unique if n > 0)
    
    
    
nums = [1,2,3,4,5]
solution = Solution()
result = solution.maxSum(nums)
print(result)