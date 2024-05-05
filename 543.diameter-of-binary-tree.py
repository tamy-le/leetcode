#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def diameter(root):
            if not root:
                return 0
            left = diameter(root.left)
            right = diameter(root.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        diameter(root)
        return self.diameter


# @lc code=end
# Time: O(n)
# Memory: O(1)
