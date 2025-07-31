class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = set()
        cur = set()
        
        for num in arr:
            next_cur = {num}
            for prev in cur:
                next_cur.add(prev | num)
            cur = next_cur
            res.update(cur)
        
        return len(res)
    
    
    
arr = [1,1,2]
solution = Solution()
result = solution.subarrayBitwiseORs(arr)
print(result)