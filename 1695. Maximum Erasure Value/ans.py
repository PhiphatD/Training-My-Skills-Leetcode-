class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        left = 0
        current = 0
        maxsum = 0
        for right in range(len(nums)):
            while nums[right]  in seen:
                seen.remove(nums[left])
                current -= nums[left]
                left += 1
            seen.add(nums[right])
            current += nums[right]
            maxsum = max(current,maxsum)
        return maxsum
        
        return nums
        
nums = [4,2,4,5,6]
solution = Solution()
result = solution.maximumUniqueSubarray(nums)
print(result)  # Output: 0 (or the expected output based on the implementation)