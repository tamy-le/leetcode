# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

        def reverse(head):
            previous = None
            next = head
            while next:
                cur = next
                next = next.next
                cur.next = previous
                previous = cur
            return previous

        def divide_half(head):
            slow = head
            fast = head
            previous = None
            while fast and fast.next:
                fast = fast.next.next
                previous = slow
                slow = slow.next
            previous.next = None
            return slow

        def merge(head1, head2):
            while head1 and head2:
                temp = head1.next
                head1.next = head2
                head2 = head2.next
                head1 = head1.next
                if not temp:
                    head1.next = head2
                    return
                head1.next = temp
                head1 = temp

        result = head
        if head.next == None or head.next.next == None:
            return head

        middle_node = divide_half(head)
        reverse_half = reverse(middle_node)
        merge(head, reverse_half)
        return result


# @lc code=end
# Time: O(n)
# Memory: O(1)
