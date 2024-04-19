# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        next_node = head
        while next_node:
            curr = next_node
            next_node = next_node.next
            curr.next = previous_node
            previous_node = curr
        return previous_node
        
#Time: O(n)
#Memory: O(1)