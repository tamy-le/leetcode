# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        result_l = ListNode()
        cursor_result = result_l
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            current_sum = val1 + val2 + remainder
            remainder = 0
            if current_sum > 9:
                remainder = 1
                current_sum -= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cursor_result.val = current_sum
            if l1 or l2:
                cursor_result.next = ListNode()
                cursor_result = cursor_result.next
        if remainder:
            cursor_result.next = ListNode(remainder)
        return result_l

#Time: O(n)
#Memory: O(1) Exclude the result linked list