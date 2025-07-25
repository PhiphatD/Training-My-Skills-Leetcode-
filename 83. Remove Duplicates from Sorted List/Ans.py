class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next



class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(head.val)
        current = dummy
        
        while head :
            if current.val == head.val :
                head = head.next
            elif current.val != head.val :
                current.next = ListNode(head.val)
                current = current.next
                head = head.next

        return dummy





head = [1,1,2] 
solution = Solution()
head = create_linked_list(head)
result = solution.deleteDuplicates(head)


