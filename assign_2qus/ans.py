# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        
        nums = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == k:
                # พบคู่แล้ว
                return True
            elif s < k:
                left += 1
            else:
                right -= 1
        return False

def create_tree_from_list(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root


list = [5,3,6,2,4,None,7]
target = 9
solution = Solution()
root = create_tree_from_list(list)
result = solution.findTarget(root, target)
print(result)  # Output: True

