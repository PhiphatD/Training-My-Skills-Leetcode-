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
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode(0)
        curr = result
        while list1 and list2 :
            if list1.val <= list2.val :
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next               
            else :
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
        curr.next = list1 or list2
        return result.next


list1 = [1,2,4]
list2 = [1,3,4]

linklist1 = create_linked_list(list1)
linklist2 = create_linked_list(list2)
solution = Solution()
result = solution.mergeTwoLists(linklist1,linklist2)
print(result)