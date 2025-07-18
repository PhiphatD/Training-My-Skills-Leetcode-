class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_set = ""
        max_len = 0
        for i in s :
            if i in word_set:
                idx = word_set.index(i)
                word_set = word_set[idx+1:] + i
            else:
                word_set += i 
            max_len = max(max_len, len(word_set))
        return max_len
    
s = "dvdf"
solotion = Solution()
leght = solotion.lengthOfLongestSubstring(s)
print(leght)