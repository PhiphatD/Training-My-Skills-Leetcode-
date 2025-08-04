from collections import defaultdict

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        start = 0
        max_len = 0
        fruit_count = defaultdict(int)

        for end in range(len(fruits)):
            fruit_count[fruits[end]] += 1

            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
    

fruits = [1,2,1]
    
solution = Solution()
result = solution.totalFruit(fruits)
print(result)