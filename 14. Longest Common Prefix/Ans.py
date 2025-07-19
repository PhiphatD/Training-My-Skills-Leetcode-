class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: stri
        """
        longest = strs[0]
        if len(strs) == 1 :
            return strs[0]
        for i in strs[1:]:
            while not i.startswith(longest):
                longest = longest[:-1]
                if longest == "":
                    return ""
        return longest
    
strs = ["dog","doa"]
solution = Solution()
result = solution.longestCommonPrefix(strs)
print(result)