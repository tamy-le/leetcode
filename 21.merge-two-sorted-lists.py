# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        next_node = result
        while list1 and list2:
            if list1.val < list2.val:
                next_node.next = list1
                list1 = list1.next
            else:
                next_node.next = list2
                list2 = list2.next
            next_node = next_node.next
        while list1:
            next_node.next = list1
            list1 = list1.next
            next_node = next_node.next
        while list2:
            next_node.next = list2
            list2 = list2.next
            next_node = next_node.next
        return result.next
# Time: O(n+m)
# Memory: O(1)