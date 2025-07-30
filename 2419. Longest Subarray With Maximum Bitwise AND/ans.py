class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)
        max_streak = max(
            len(list(values))
            for key, values in groupby(nums)
            if key == max_val
        )
        return max_streak