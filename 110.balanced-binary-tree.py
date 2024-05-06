#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            if abs(left - right) > 1 or left == -1 or right == -1:
                return -1
            return 1 + max(left, right)

        return height(root) != -1


# Time: O(n)
# Memory: O(1)
# @lc code=end
