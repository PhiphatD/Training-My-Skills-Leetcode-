class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return Counter(str(n)) in (Counter(str(1<<i)) for i in range(30))
    