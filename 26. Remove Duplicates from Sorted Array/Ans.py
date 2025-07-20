class Solution(object):
    def removeDuplicates(self, nums):

        q = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] :
                nums[q] = nums[i]
                q = q + 1
        return q
        
        
nums = [1,1,2]
solution = Solution()
result = solution.removeDuplicates(nums)
print(result)