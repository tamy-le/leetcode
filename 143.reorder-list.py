#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None or head.next.next == None:
            return head

        next_node = head.next.next
        traverse_node = head
        previous_node = head.next
        while traverse_node.next:
            if next_node == None:
                return head
            if next_node.next == None:
                previous_node.next = None
                next_node.next = traverse_node.next
                traverse_node.next = next_node
                traverse_node = next_node.next
                next_node = traverse_node.next
                if next_node == None:
                    return head
            previous_node = next_node
            next_node = next_node.next
        return head


# @lc code=end
# Time: O(n^2)
# Memory: o(1)
