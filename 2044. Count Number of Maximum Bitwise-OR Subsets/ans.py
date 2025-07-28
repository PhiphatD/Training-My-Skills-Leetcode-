class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxOR = 0
        for num in nums:
            maxOR |= num

        def backtrack(index, currentOR):
            if index == len(nums):
                return 1 if currentOR == maxOR else 0

            if currentOR == maxOR:
                return 1 << (len(nums) - index)

            return backtrack(index + 1, currentOR | nums[index]) + \
                   backtrack(index + 1, currentOR)

        return backtrack(0, 0)

nums = [3,2,1,5]
solution = Solution()
result = solution.countMaxOrSubsets(nums)
print(result)